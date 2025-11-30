#this is main file for cag project
from fastapi import FastAPI,HTTPException
from fastapi.responses import HTMLResponse
import uvicorn
import data_handler


app=FastAPI(
    title="CAG Project API,Chat with Your PDFs.",
    description="You can upload,chat update your existing pdf with new one and can delete it.",
    version="1.0.0"
)

app.include_router(
  data_handler.router,
    prefix="/api/v1",
    tags=["Data Handling and chat with PDF"]
)

@app.get("/",response_class=HTMLResponse,tags=["Root"])
def read_root():
    """"provide a link to wagger UI."""
    html_content="""<head>
    <title>CAG Project API</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            padding: 2rem; 
            background: #f9f9f9; 
        }
        .container { 
            max-width: 600px; 
            margin: auto; 
            background: #fff; 
            padding: 2rem; 
            border-radius: 8px; 
        }
        h1 { 
            color: #333; 
        }
        a { 
            color: #007acc; 
            text-decoration: none; 
        }
        a:hover { 
            text-decoration: underline; 
        }
    </style>
</head>
<body><div class="container">
    <h1>Welcome to the CAG Project API</h1>
    <p>👉 View the automatically generated API documentation here:</p>
    <p><a href="/docs" target="_blank">Swagger UI (OpenAPI Docs)</a></p>
</div>
</body>
</html>
</body>
    
    </html>"""
    return HTMLResponse(content=html_content,status_code=200)

if __name__=="__main__":
     uvicorn.run("main1:app",host="127.0.0.1",port=8000)