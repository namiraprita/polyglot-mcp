import os
from typing import Optional
import anthropic
from dotenv import load_dotenv

from .models import TranslationRequest, TranslationResponse

class PolyglotClient:
    def __init__(self, api_key: Optional[str] = None):
        load_dotenv()
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY must be provided either as an argument or environment variable")
        
        self.client = anthropic.Anthropic(api_key=self.api_key)

    def _create_prompt(self, request: TranslationRequest) -> str:
        domain_context = {
            "legal": "legal and contractual",
            "medical": "medical and healthcare",
            "general": "general"
        }
        
        formality_context = {
            "formal": "formal and professional",
            "informal": "casual and conversational"
        }
        
        prompt = f"""You are a professional translator. Please translate the following text from {request.metadata.source_language} to {request.metadata.target_language}.
        
Domain: {domain_context[request.metadata.domain]}
Formality: {formality_context[request.metadata.formality]}

Text to translate:
{request.data['text']}

Please provide only the translation without any additional explanation or context."""

        return prompt

    def translate(self, request: TranslationRequest) -> TranslationResponse:
        prompt = self._create_prompt(request)
        
        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            temperature=0.7,
            system="You are a professional translator. Provide accurate translations while maintaining the appropriate tone and domain-specific terminology.",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        translated_text = message.content[0].text.strip()
        
        return TranslationResponse(
            metadata=request.metadata,
            data={"text": translated_text}
        )
    
    def simple_translate(
        self, 
        text: str, 
        source_language: str, 
        target_language: str, 
        domain: str = "general", 
        formality: str = "informal"
    ) -> str:
        """Simplified translation method that returns just the translated text"""
        
        domain_context = {
            "legal": "legal and contractual",
            "medical": "medical and healthcare", 
            "general": "general"
        }
        
        formality_context = {
            "formal": "formal and professional",
            "informal": "casual and conversational"
        }
        
        prompt = f"""You are a professional translator. Please translate the following text from {source_language} to {target_language}.
        
Domain: {domain_context[domain]}
Formality: {formality_context[formality]}

Text to translate:
{text}

Please provide only the translation without any additional explanation or context."""

        message = self.client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1000,
            temperature=0.7,
            system="You are a professional translator. Provide accurate translations while maintaining the appropriate tone and domain-specific terminology.",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        
        return message.content[0].text.strip() 