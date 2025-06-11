# Polyglot - Model Context Protocol for Translation

Polyglot is an MCP (Model Context Protocol) server that provides translation services using Claude Sonnet 3.5.

## Supported Languages

- Arabic (ar)
- Chinese (zh) 
- English (en)
- French (fr)
- Russian (ru)
- Spanish (es)

## Features

- Multiple transport options (stdio, SSE)
- Support for multiple domains (legal, medical, general)
- Formality level control (formal/informal)
- Claude Sonnet 3.5 integration
- API key authentication

## Installation

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv pip install .
```

## Configuration

Create a `.env` file in your project root:
```bash
ANTHROPIC_API_KEY=your_api_key_here
```

## Transport Options

### 1. STDIO Transport (For Claude Desktop Integration)

Use `server.py` for stdio transport:

```bash
uv run server.py
```

### 2. SSE Transport (For HTTP/Web Usage)

Use `server_sse.py` for SSE transport:

```bash
uv run server_sse.py
```

This runs on port 8001 with SSE transport for web/API usage.

## Testing

### 1. With Claude Desktop (STDIO Transport)

Add this configuration to your Claude Desktop config:

```json
"polyglot": {
  "command": "/usr/bin/env",
  "args": [
    "uv",
    "run",
    "/Users/namirasuniaprita/Documents/GitHub/polyglot-mcp/polyglot-mcp/start_mcp_server.py"
  ],
  "env": {
    "ANTHROPIC_API_KEY": "your_api_key_here",
    "PYTHONPATH": "/Users/namirasuniaprita/Documents/GitHub/polyglot-mcp/polyglot-mcp",
    "PATH": "/Users/namirasuniaprita/.local/bin:/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin:/usr/sbin:/sbin"
  }
}
```

### 2. With MCP Inspector (SSE Transport)

1. Run the SSE server:
   ```bash
   uv run server_sse.py
   ```

2. Make sure you have a `.env` file with your API key

3. Use this payload for translation requests:
   ```json
   {
     "version": "1.0",
     "type": "translation_request",
     "metadata": {
       "source_language": "en",
       "target_language": "fr",
       "domain": "general",
       "formality": "informal",
       "api_key": "your_anthropic_api_key_here"
     },
     "data": {
       "text": "Hello, how are you?"
     }
   }
   ```

## Available Tools

- `translate`: Translate text between supported languages
- `health_check`: Check service status

## Valid Values

- **Languages**: `ar`, `zh`, `en`, `fr`, `ru`, `es`
- **Domains**: `general`, `legal`, `medical`
- **Formality**: `formal`, `informal`

## License

MIT License
