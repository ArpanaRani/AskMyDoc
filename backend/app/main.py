from fastapi import FastAPI
from app.api.documents import router as documents_router


app = FastAPI(
    title="AskMyDocs API",
    description="Local AI-powered document assistant using RAG",
    version="1.0.0"
)


app.include_router(documents_router)



# Welcome endpoint
@app.get("/")
def root():
    return {
        "message": "Welcome to My First AI Application",
        "status": "running"
    }


# Health check endpoint
@app.get("/runningStatus")
def health_check():
    return {
        "status": "Running",
        "application": "AskMyDocs"
    }
