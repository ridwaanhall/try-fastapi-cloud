from fastapi import FastAPI, status
from pydantic import BaseModel

class MessageResponse(BaseModel):
    message: str

app = FastAPI(
    title="Professional API",
    version="0.0.2",
    description="A more advanced and professional FastAPI application.",
    contact={
        "name": "API Support",
        "email": "support@example.com",
    },
    docs_url="/docs",
    redoc_url="/redoc"
)

@app.get(
    "/",
    response_model=MessageResponse,
    status_code=status.HTTP_200_OK,
    summary="Root Endpoint",
    tags=["Root"],
    response_description="A welcome message."
)
async def read_root() -> MessageResponse:
    """Root endpoint that returns a professional welcome message."""
    return MessageResponse(message="Welcome to the Professional API.")
