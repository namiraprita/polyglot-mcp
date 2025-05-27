from mcp.server.fastmcp import FastMCP
from .models import TranslationRequest, TranslationResponse
from .client import PolyglotClient

# Initialize FastMCP server
mcp = FastMCP("polyglot", port=8001)

client = PolyglotClient()

@mcp.tool()
def translate(request: TranslationRequest) -> TranslationResponse:
    """
    Translate text between languages using Claude Sonnet 3.5.
    
    Args:
        request: TranslationRequest containing source language, target language,
                domain, formality level and text to translate
                
    Returns:
        TranslationResponse containing the translated text
    """
    try:
        return client.translate(request)
    except Exception as e:
        raise Exception(f"Translation failed: {str(e)}")

@mcp.resource("health")
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