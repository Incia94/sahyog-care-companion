from fastapi import FastAPI

app = FastAPI(
    title="Sahyog Care Companion",
    version="0.1.0"
)

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "sahyog-care-companion"
    }