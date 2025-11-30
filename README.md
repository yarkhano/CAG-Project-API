# The CAG Fast API Project 

This project is a backend API developed using FastAPI. It gives you the ability to chat with your documents by uploading them and asking questions based on their content.

The term **CAG** stands for **Cache Argumented Generation**. The model stores your document text in a temporary memory (a cache) to use as context when answering your queries.

The project uses a clean architecture, separating logic into five different Python files managed with FastAPI's API Routers. The homepage (`/`) uses simple HTML and CSS to provide a welcome screen and a link to the main API documentation.

---

## Features

* **Upload PDFs:** Store a new document under a unique ID (UUID).
* **Chat with Documents:** Ask questions (queries) directed at a specific document.
* **Update Documents:** Append the text from a new PDF to an existing document.
* **Delete Documents:** Remove a document from the in-memory cache.
* **List Documents:** See all document IDs currently stored.

---

## Project Structure

The project is broken into 5 main files for better organization:

* `main.py`: The main FastAPI application file. It starts the server and includes the router.
* `data_handler.py`: Contains all the API endpoints (using `APIRouter`) for uploading, querying, etc.
* `client_llm.py`: Manages the connection to the Google Gemini API.
* `pdf_processor.py`: A utility file to extract text from PDF documents.
* `data_stores.py`: A simple in-memory Python dictionary used as a temporary database.

---

## 🚀 Installation & Setup

Follow these steps to get the project running on your local machine.

### 1. Prerequisites

You must have Python 3.7+ installed.

### 2. Clone the Repository

(If your project is on GitHub, add the link here. Otherwise, just make sure you are in the project folder.)

```bash
git clone [https://github.com/your-username/your-project-name.git](https://github.com/your-username/your-project-name.git)
cd your-project-name
3. Install Dependencies
It's recommended to use a virtual environment.

# Create a virtual environment
python -m venv venv

# Activate it (on Windows)
.\venv\Scripts\activate
# (on Mac/Linux)
# source venv/bin/activate

# Install the required libraries
pip install fastapi "uvicorn[standard]" google-generativeai pypdf

4. Add Your API Key
This project requires a Google Gemini API key to function.

Open the client_llm.py file.
Find the line: api_key = "YOUR_API_KEY_GOES_HERE"
Paste your personal API key directly into the quotes.
5. Run the Application
Once installed, run the server with uvicorn:

uvicorn main:app --reload
The --reload flag means the server will automatically restart if you make any changes to the code.

Usage
Once the server is running, you can access the API in two ways:

1. Welcome Page
Go to http://127.0.0.1:8000/ in your browser to see the HTML welcome page.

2. API Docs (Swagger UI)
This is the main way to interact with the API. Go to:

http://127.0.0.1:8000/docs

FastAPI automatically generates this interactive page. From here, you can test all the endpoints.

Recommended Workflow:

Go to the POST /api/v1/upload endpoint.
Click "Try it out."
Generate a UUID (you can use an online UUID generator) and paste it into the uuid field.
Upload a PDF file.
Click "Execute."
Now, copy that same UUID.
Go to the GET /api/v1/query/{uuid} endpoint, click "Try it out," paste the uuid, and type your question in the query field.
Click "Execute" to get your answer.
API Endpoints
Here are the main endpoints for the service:

POST /api/v1/upload: Upload a new PDF. Requires a UUID and a .pdf file.
PUT /api/v1/upload/{uuid}: Append a new PDF's text to an existing document.
GET /api/v1/query/{uuid}: Ask a question (query) about a specific document.
DELETE /api/v1/delete/{uuid}: Delete a document from the data store.
GET /api/v1/alluuids: Get a list of all document UUIDs currently in memory.
⚠️ Important Note on Data Storage
This project uses a simple Python dictionary (data_store = {}) for storage. This means all your uploaded data will be completely erased every time you restart the Python server. This is fine for development and testing, but for a real application, you would need to connect a permanent database.
