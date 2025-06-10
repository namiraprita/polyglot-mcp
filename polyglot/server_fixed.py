from mcp.server.fastmcp import FastMCP
from polyglot.client import PolyglotClient
import os
from dotenv import load_dotenv
import sys

# Load environment variables
load_dotenv()

# Initialize FastMCP server for stdio transport
mcp = FastMCP("polyglot")

# Initialize client with server's API key
SERVER_API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not SERVER_API_KEY:
    print("Error: ANTHROPIC_API_KEY environment variable is required", file=sys.stderr)
    sys.exit(1)

client = PolyglotClient(api_key=SERVER_API_KEY)

@mcp.tool()
def translate(
    text: str,
    source_language: str = "en",
    target_language: str = "fr", 
    domain: str = "general",
    formality: str = "informal"
) -> str:
    """
    Translate text between languages using Claude Sonnet 3.5.
    
    Args:
        text: The text to translate
        source_language: Source language code (ar, zh, en, fr, ru, es)
        target_language: Target language code (ar, zh, en, fr, ru, es)  
        domain: Translation domain (general, legal, medical)
        formality: Formality level (formal, informal)
                
    Returns:
        The translated text
        
    Raises:
        Exception: If translation fails
    """
    try:
        # Validate language codes
        valid_languages = ["ar", "zh", "en", "fr", "ru", "es"]
        if source_language not in valid_languages:
            raise ValueError(f"Invalid source language. Must be one of: {', '.join(valid_languages)}")
        if target_language not in valid_languages:
            raise ValueError(f"Invalid target language. Must be one of: {', '.join(valid_languages)}")
            
        # Validate domain
        valid_domains = ["general", "legal", "medical"]
        if domain not in valid_domains:
            raise ValueError(f"Invalid domain. Must be one of: {', '.join(valid_domains)}")
            
        # Validate formality
        valid_formality = ["formal", "informal"]
        if formality not in valid_formality:
            raise ValueError(f"Invalid formality. Must be one of: {', '.join(valid_formality)}")
        
        # Use the simplified client method
        result = client.simple_translate(
            text=text,
            source_language=source_language,
            target_language=target_language,
            domain=domain,
            formality=formality
        )
        
        return result
        
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
    # Initialize and run the server with stdio transport for Claude Desktop
    mcp.run(transport='stdio')