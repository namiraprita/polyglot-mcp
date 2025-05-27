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

## Usage

```python
from polyglot import TranslationRequest, PolyglotClient

# Create a translation request
request = TranslationRequest(
    source_language="fr",
    target_language="en",
    domain="legal",
    formality="formal",
    text="Le contrat a été signé hier à Genève."
)

# Initialize the client
client = PolyglotClient()

# Send the request
response = client.translate(request)
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