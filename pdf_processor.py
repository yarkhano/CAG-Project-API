from pypdf import PdfReader

def data_extract_from_pdf(pdf_path: str) -> str:
    try:
        reader = PdfReader(pdf_path)
        full_text = []

        for page in reader.pages:
            text = page.extract_text()
            if text:
                full_text.append(text)

        # Join all extracted pages into one string
        return "\n".join(full_text)

    except Exception as e:
        print("PDF extraction error:", e)
        return ""
