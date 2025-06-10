#!/usr/bin/env python3
"""
Simplified Polyglot Translation Service for MCP
This version focuses on basic functionality to ensure connection works
"""

import sys
import os
import logging

# Add project directory to path
project_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(project_dir))

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    from mcp.server.fastmcp import FastMCP
    from dotenv import load_dotenv
    import anthropic
    
    logger.info("All imports successful")
    
    # Load environment variables
    load_dotenv()
    
    # Initialize FastMCP server
    mcp = FastMCP("polyglot")
    logger.info("FastMCP server initialized")
    
    # Get API key
    SERVER_API_KEY = os.getenv("ANTHROPIC_API_KEY")
    if not SERVER_API_KEY:
        logger.error("ANTHROPIC_API_KEY environment variable is required")
        raise ValueError("ANTHROPIC_API_KEY environment variable is required")
    
    logger.info("API key loaded successfully")
    
    # Initialize Anthropic client
    client = anthropic.Anthropic(api_key=SERVER_API_KEY)
    logger.info("Anthropic client initialized")
    
    @mcp.tool()
    def translate(
        text: str,
        source_language: str = "en",
        target_language: str = "fr", 
        domain: str = "general",
        formality: str = "informal"
    ) -> str:
        """
        Translate text between languages using Claude.
        
        Args:
            text: The text to translate
            source_language: Source language code (ar, zh, en, fr, ru, es)
            target_language: Target language code (ar, zh, en, fr, ru, es)  
            domain: Translation domain (general, legal, medical)
            formality: Formality level (formal, informal)
                    
        Returns:
            The translated text
        """
        logger.info(f"Translation request: '{text}' from {source_language} to {target_language}")
        
        try:
            # Validate inputs
            valid_languages = ["ar", "zh", "en", "fr", "ru", "es"]
            valid_domains = ["general", "legal", "medical"]
            valid_formality = ["formal", "informal"]
            
            if source_language not in valid_languages:
                raise ValueError(f"Invalid source language. Must be one of: {', '.join(valid_languages)}")
            if target_language not in valid_languages:
                raise ValueError(f"Invalid target language. Must be one of: {', '.join(valid_languages)}")
            if domain not in valid_domains:
                raise ValueError(f"Invalid domain. Must be one of: {', '.join(valid_domains)}")
            if formality not in valid_formality:
                raise ValueError(f"Invalid formality. Must be one of: {', '.join(valid_formality)}")
            
            # Create translation prompt
            prompt = f"""Translate the following text from {source_language} to {target_language}.
            
Domain: {domain}
Formality: {formality}
Text: {text}

Provide only the translation without explanation."""

            # Make API call
            message = client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1000,
                temperature=0.3,
                messages=[{"role": "user", "content": prompt}]
            )
            
            result = message.content[0].text.strip()
            logger.info(f"Translation successful: '{result}'")
            return result
            
        except Exception as e:
            logger.error(f"Translation failed: {str(e)}")
            raise Exception(f"Translation failed: {str(e)}")
    
    @mcp.tool()
    def health_check() -> str:
        """Check if the translation service is healthy."""
        logger.info("Health check requested")
        return "Polyglot translation service is healthy and ready!"
    
    @mcp.resource("polyglot://health")
    def health_resource() -> str:
        """Health check resource."""
        return "Service is healthy"
    
    logger.info("All tools and resources registered successfully")
    
    if __name__ == "__main__":
        logger.info("Starting MCP server...")
        mcp.run(transport='stdio')
        
except Exception as e:
    logger.error(f"Server initialization failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
