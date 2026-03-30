from fastapi import FastAPI, Response, status

app = FastAPI(title="My API", version="1.0.0")

@app.get("/", response_model=dict, status_code=status.HTTP_200_OK, summary="Root Endpoint")
def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the API."}
