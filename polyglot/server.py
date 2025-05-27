from fastapi import FastAPI, HTTPException
from .models import TranslationRequest, TranslationResponse
from .client import PolyglotClient

app = FastAPI(
    title="Polyglot Translation API",
    description="A Model Contexts Protocol implementation for translation services",
    version="1.0.0"
)

client = PolyglotClient()

@app.post("/translate", response_model=TranslationResponse)
async def translate(request: TranslationRequest) -> TranslationResponse:
    try:
        return client.translate(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"} 