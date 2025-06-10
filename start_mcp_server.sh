#!/bin/bash

# This script starts the MCP server using uv
# It is meant to be used directly by Claude Desktop

# Set the working directory
cd /Users/namirasuniaprita/Documents/GitHub/polyglot-mcp/polyglot-mcp

# Activate virtual environment (not needed with uv run)
# source .venv/bin/activate

# Run the server
uv run polyglot/server_fixed.py
