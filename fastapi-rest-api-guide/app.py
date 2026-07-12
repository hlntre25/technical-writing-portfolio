from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional
import uuid

app = FastAPI(
    title="Portfolio Document API",
    description="A demo API for a technical writing portfolio.",
    version="1.0.0",
)

# In-memory database
db = {}

class DocumentInput(BaseModel):
    title: str = Field(..., example="Quarterly Report")
    format: str = Field(..., example="pdf")
    template: Optional[str] = Field(None, example="business-report")

class DocumentOutput(BaseModel):
    id: str
    title: str
    format: str
    template: Optional[str]
    status: str = "completed"

@app.post("/documents", response_model=DocumentOutput, status_code=201)
def create_document(document: DocumentInput):
    """
    Create a new document.
    """
    doc_id = str(uuid.uuid4())
    new_doc = DocumentOutput(id=doc_id, **document.dict())
    db[doc_id] = new_doc
    return new_doc

@app.get("/documents", response_model=List[DocumentOutput])
def list_documents():
    """
    List all available documents.
    """
    return list(db.values())

@app.get("/documents/{document_id}", response_model=DocumentOutput)
def get_document(document_id: str):
    """
    Retrieve a single document by its ID.
    """
    if document_id not in db:
        raise HTTPException(status_code=404, detail="Document not found")
    return db[document_id]

@app.delete("/documents/{document_id}", status_code=204)
def delete_document(document_id: str):
    """
    Delete a document by its ID.
    """
    if document_id not in db:
        raise HTTPException(status_code=404, detail="Document not found")
    del db[document_id]
    return

@app.get("/health")
def health_check():
    """
    Health check endpoint.
    """
    return {"status": "ok"}
