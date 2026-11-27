from fastapi import APIRouter , File, UploadFile
from app.services.pdf_service import extract_text_from_pdf
from app.rag.chunking import chunk_pages

router = APIRouter(prefix="/documents", tags=["Document"])
@router.post("/upload")

async def upload_document(file: UploadFile = File(...)):
    content = await file.read()

    extracted_pages = extract_text_from_pdf(content)

  
    # Split extracted PDF text into chunks
    chunks = chunk_pages(extracted_pages)

    return {
        "filename": file.filename,
        "total_pages": len(extracted_pages),
        "extracted_pages": extracted_pages,
        "total_chunks": len(chunks),
        "chunks": chunks,
        "message": "PDF uploaded, text extracted and chunked successfully"
    }
