from mcp.server.fastmcp import FastMCP
from polyglot.models import TranslationRequest, TranslationResponse
from polyglot.client import PolyglotClient
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastMCP server
mcp = FastMCP("polyglot", port=8001)

# Get API key from environment
VALID_API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not VALID_API_KEY:
    raise ValueError("ANTHROPIC_API_KEY environment variable is required")

client = PolyglotClient()

@mcp.tool()
def translate(request: TranslationRequest) -> TranslationResponse:
    """
    Translate text between languages using Claude Sonnet 3.5.
    
    Args:
        request: TranslationRequest containing source language, target language,
                domain, formality level, API key and text to translate
                
    Returns:
        TranslationResponse containing the translated text
        
    Raises:
        Exception: If API key is invalid or translation fails
    """
    # Validate API key
    if request.metadata.api_key != VALID_API_KEY:
        raise Exception("Invalid API key")
        
    try:
        return client.translate(request)
    except Exception as e:
        raise Exception(f"Translation failed: {str(e)}")

@mcp.resource("polyglot://health")
def health_check() -> str:
    """
    Check if the translation service is healthy.
    
    Returns:
        A string indicating the service status
    """
    return "Service is healthy"

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='sse') 