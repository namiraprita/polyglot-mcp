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
    api_key: str = Field(..., description="API key for authentication")

class SimpleTranslationMetadata(BaseModel):
    """Metadata for user requests - no API key required"""
    source_language: Language
    target_language: Language
    domain: Domain
    formality: Formality
    
    def copy(self) -> 'TranslationMetadata':
        """Convert to full TranslationMetadata (server will add API key)"""
        return TranslationMetadata(
            source_language=self.source_language,
            target_language=self.target_language,
            domain=self.domain,
            formality=self.formality,
            api_key=""  # Will be set by server
        )

class TranslationRequest(BaseModel):
    version: Literal["1.0"] = "1.0"
    type: Literal["translation_request"] = "translation_request"
    metadata: TranslationMetadata
    data: dict[str, str] = Field(..., description="Contains the text to translate")

class SimpleTranslationRequest(BaseModel):
    """Simplified request model for users - no API key required"""
    version: Literal["1.0"] = "1.0"
    type: Literal["translation_request"] = "translation_request"
    metadata: SimpleTranslationMetadata
    data: dict[str, str] = Field(..., description="Contains the text to translate")

class TranslationResponse(BaseModel):
    version: Literal["1.0"] = "1.0"
    type: Literal["translation_response"] = "translation_response"
    metadata: TranslationMetadata
    data: dict[str, str] = Field(..., description="Contains the translated text")
    status: str = "success" 