import sys
import json
from typing import Dict, Any

def send_message(message: Dict[str, Any]) -> None:
    """Send a message to the MCP server via stdout"""
    message_json = json.dumps(message)
    header = f"Content-Length: {len(message_json)}\r\n\r\n"
    sys.stdout.write(header + message_json)
    sys.stdout.flush()

def main():
    # Test the health resource
    health_request = {
        "id": "1",
        "method": "mcp/resource",
        "params": {
            "uri": "polyglot://health"
        }
    }
    send_message(health_request)

    # Test the translate tool
    translate_request = {
        "id": "2",
        "method": "mcp/invoke",
        "params": {
            "tool": "translate",
            "parameters": {
                "text": "Hello, how are you?",
                "source_language": "en",
                "target_language": "fr",
                "domain": "general",
                "formality": "informal"
            }
        }
    }
    send_message(translate_request)

if __name__ == "__main__":
    main()
