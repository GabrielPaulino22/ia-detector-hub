from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from .utils import detect_ai_text, extract_text_from_pdf, generate_pdf_report
import tempfile

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze_text(text: str = Form(None), file: UploadFile = File(None)):
    if file:
        temp_path = tempfile.NamedTemporaryFile(delete=False).name
        with open(temp_path, "wb") as f:
            f.write(await file.read())
        text = extract_text_from_pdf(temp_path)

    return detect_ai_text(text)

@app.get("/download_report")
def download_report():
    return FileResponse(generate_pdf_report())
