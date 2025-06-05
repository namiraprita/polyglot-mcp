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
- API key authentication

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

## Configuration

1. Create a `.env` file in your project root:
```bash
ANTHROPIC_API_KEY=your_api_key_here
```

2. Make sure to keep your API key secure and never commit it to version control.

## Running the MCP Server

To run the MCP server, use the following command:

```bash
uv run polyglot/server.py
```

This will start the server on the configured port (default: 8001).

## Testing the MCP Server

You can test the MCP server using a simple client script. For example, to test the health check resource, create a file named `test_client.py` with the following content:

```python
import requests

response = requests.get("http://localhost:8001/health")
print(response.text)
```

Run the test client with:

```bash
uv run test_client.py
```

You should see the output: "Service is healthy".

## Environment Variables

Make sure to set your Anthropic API key in a `.env` file in the project root:

```
ANTHROPIC_API_KEY=your_api_key_here
```

## Additional Notes

- The server uses the Model Context Protocol (MCP) to expose tools and resources.
- Ensure all dependencies are installed using `uv` or `pip`.
- For more details, refer to the project documentation.

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
    "formality": "formal",
    "api_key": "your_api_key_here"  // Required for authentication
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