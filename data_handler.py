# this is one of the file for cag project
import os
import uuid as uuid_pkg
from fastapi import APIRouter, HTTPException, UploadFile, File, Query

# FIX: Assuming your files are named this, these imports are correct.
from data_stores import data_store
from pdf_processor import data_extract_from_pdf
from client_llm import get_llm_response

UPLOAD_DIR = "temp_uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

router = APIRouter()


@router.post("/upload")
def upload_data(uuid: uuid_pkg.UUID, file: UploadFile = File(...)):
    uuid_str = str(uuid)
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=405, detail="You selected file type other than PDF, kindly select PDF file!")

    # FIX: This logic is now correct for a POST request.
    if uuid_str in data_store:
        raise HTTPException(status_code=404, detail="UUID is already in list.")
    else:
        # FIX: All code for the 'else' block must be indented.
        file_path = os.path.join(UPLOAD_DIR, f"{uuid_str}_upload_{file.filename}")
        try:
            # The 'with' block opens, writes, and *closes* the file.
            with open(file_path, "wb") as f:
                f.write(file.file.read())

            # FIX: Moved this line *outside* the 'with' block.
            # You must wait for the file to be closed before you can read it.
            new_text = data_extract_from_pdf(file_path)

            if not new_text:
                raise HTTPException(status_code=404, detail="File not found or is empty")
            else:
                data_store[uuid_str] = new_text
                # FIX: Added a success message
                return {"message": "File uploaded successfully!", "uuid": uuid_str}

        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

        finally:
            if os.path.exists(file_path):
                os.remove(file_path)


@router.put("/upload/{uuid}", status_code=201)
def upload_pdf(uuid: uuid_pkg.UUID, file: UploadFile = File(...)):
    # FIX: All code for the function must be indented.
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=405, detail="You selected file type other than PDF, kindly select PDF file!")

    uuid_str = str(uuid)
    if uuid_str not in data_store:
        raise HTTPException(
            status_code=400,
            detail="not found use post ap/v1/upload{uuid_str} to create a file. "
        )

    file_path = os.path.join(UPLOAD_DIR, f"{uuid_str}_update_{file.filename}")

    try:
        with open(file_path, "wb") as buffer:
            buffer.write(file.file.read())

        # FIX: Moved this line *outside* the 'with' block.
        new_text = data_extract_from_pdf(file_path)

        if new_text is None:
            raise HTTPException(status_code=404, detail="No text is extracted.")

        data_store[uuid_str] += "\n\n" + new_text
        return {"message": "Data append successfully!"}

    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)


@router.get("/query/{uuid}")
def query(uuid: uuid_pkg.UUID, query: str = Query(..., min_length=1)):
    # FIX: All code for the function must be indented.
    uuid_str = str(uuid)
    if uuid_str not in data_store:
        raise HTTPException(status_code=404, detail="No uuid exist in such a name!")

    store_text = data_store[uuid_str]
    try:
        llm_response = get_llm_response(context=store_text, query=query)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"not processed!:{e}")


    return {"uuid": uuid_str, "query": query, "llm_response": llm_response}




@router.delete("/delete/{uuid}")
def delete(uuid: uuid_pkg.UUID):
    # FIX: All code for the function must be indented.
    uuid_str = str(uuid)

    if uuid_str not in data_store:
        raise HTTPException(status_code=404, detail="No uuid exist in such a name!")
    else:
        del data_store[uuid_str]

    return {"message": "Data delete successfully!"}


@router.get("/alluuids")
def show_ids():
    # FIX: Code for the function must be indented.
    return list(data_store.keys())