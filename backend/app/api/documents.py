from fastapi import APIRouter , File, UploadFile
from app.services.pdf_service import extract_text_from_pdf

router = APIRouter(prefix="/documents", tags=["Document"])
@router.post("/upload")

async def upload_document(file: UploadFile = File(...)):
    content = await file.read()

    extracted_pages = extract_text_from_pdf(content)

    return {
        "filename": file.filename,
        "extracted_pages": extracted_pages,
        "size": len(extracted_pages),
        "message": "File uploaded successfully"
    }
