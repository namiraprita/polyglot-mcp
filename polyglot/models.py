from enum import Enum
from typing import Literal
from pydantic import BaseModel, Field

class Language(str, Enum):
    ARABIC = "ar"
    CHINESE = "zh"
    ENGLISH = "en"
    FRENCH = "fr"
    RUSSIAN = "ru"
    SPANISH = "es"

class Domain(str, Enum):
    LEGAL = "legal"
    MEDICAL = "medical"
    GENERAL = "general"

class Formality(str, Enum):
    FORMAL = "formal"
    INFORMAL = "informal"

class TranslationMetadata(BaseModel):
    source_language: Language
    target_language: Language
    domain: Domain
    formality: Formality

class TranslationRequest(BaseModel):
    version: Literal["1.0"] = "1.0"
    type: Literal["translation_request"] = "translation_request"
    metadata: TranslationMetadata
    data: dict[str, str] = Field(..., description="Contains the text to translate")

class TranslationResponse(BaseModel):
    version: Literal["1.0"] = "1.0"
    type: Literal["translation_response"] = "translation_response"
    metadata: TranslationMetadata
    data: dict[str, str] = Field(..., description="Contains the translated text")
    status: str = "success" 