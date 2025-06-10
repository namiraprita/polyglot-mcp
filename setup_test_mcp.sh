#!/bin/bash

# Set up the environment
echo "Setting up the environment..."
cd /Users/namirasuniaprita/Documents/GitHub/polyglot-mcp/polyglot-mcp

# Create a virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    uv venv
fi

# Activate the virtual environment
source .venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
uv pip install -e .

# Test the server
echo "Testing the MCP server..."
uv run test_mcp.py

echo "Done! MCP server is ready for Claude Desktop."
echo "Copy the claude_desktop_config.json file to your Claude Desktop configuration directory."
