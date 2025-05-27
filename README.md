# Polyglot - Model Contexts Protocol for Translation

Polyglot is an open-source implementation of the Model Contexts Protocol (MCP) focused on translation services. It provides a standardized way to handle translation requests across multiple languages using Claude Sonnet 3.5.

## Supported Languages

- Arabic (ar)
- Chinese (zh)
- English (en)
- French (fr)
- Russian (ru)
- Spanish (es)

## Features

- Standardized translation request format
- Support for multiple domains (legal, medical, general)
- Formality level control (formal/informal)
- Claude Sonnet 3.5 integration
- MCP protocol server (via FastMCP)

## Installation

### Using uv (Recommended)

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install the package and its dependencies
uv pip install .

# For development, install with dev dependencies
uv pip install ".[dev]"
```

### Using pip

```bash
# Install the package and its dependencies
pip install .

# For development, install with dev dependencies
pip install ".[dev]"
```

## Running the MCP Server

The Polyglot MCP server uses [FastMCP](https://github.com/modelcontextprotocol/python-sdk) to expose translation tools and resources over the MCP protocol (SSE transport).

To start the server:

```bash
python -m polyglot.server
```

By default, the server will run on port 8001 using SSE transport.

## Testing the MCP Server

### Using MCP Inspector (Recommended)

1. Install the MCP Inspector:
   ```bash
   npx @modelcontextprotocol/inspector
   ```
2. Open the Inspector UI (the terminal will show a local address).
3. Set the following in the Inspector UI:
   - **Transport Type:** SSE
   - **URL:** `http://localhost:8001/sse`
   - (Optional) Set Inspector Proxy Address if needed
4. You can now interact with the translation tool and resources via the Inspector UI.

### Using a Python MCP Client

You can also interact with the server programmatically using the MCP Python SDK:

```python
from mcp.client.sse import sse_client
import asyncio

async def main():
    async with sse_client(url="http://localhost:8001/sse") as (read, write):
        # Example: call the translate tool
        request = {
            "tool": "translate",
            "args": {
                "request": {
                    "version": "1.0",
                    "type": "translation_request",
                    "metadata": {
                        "source_language": "fr",
                        "target_language": "en",
                        "domain": "legal",
                        "formality": "formal"
                    },
                    "data": {"text": "Le contrat a été signé hier à Genève."}
                }
            }
        }
        await write(request)
        response = await read()
        print(response)

asyncio.run(main())
```

## Protocol Specification

The translation request follows this JSON structure:

```json
{
  "version": "1.0",
  "type": "translation_request",
  "metadata": {
    "source_language": "fr",
    "target_language": "en",
    "domain": "legal",
    "formality": "formal"
  },
  "data": {
    "text": "Le contrat a été signé hier à Genève."
  }
}
```

## Development

To set up the development environment:

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create and activate a virtual environment
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows

# Install development dependencies
uv pip install ".[dev]"
```

## License

MIT License 