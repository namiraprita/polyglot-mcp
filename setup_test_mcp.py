#!/usr/bin/env python3

import os
import subprocess
import sys

def setup_environment():
    """Set up the environment for the MCP server"""
    print("Setting up the environment...")
    
    # Change to the project directory
    project_dir = '/Users/namirasuniaprita/Documents/GitHub/polyglot-mcp/polyglot-mcp'
    os.chdir(project_dir)
    
    # Create a virtual environment if it doesn't exist
    if not os.path.exists('.venv'):
        print("Creating virtual environment...")
        subprocess.run(['uv', 'venv'], check=True)
    
    # Install dependencies
    print("Installing dependencies...")
    subprocess.run(['uv', 'pip', 'install', '-e', '.'], check=True)
    
    print("Environment setup completed successfully!")

def test_mcp():
    """Test the MCP server"""
    print("Testing the MCP server...")
    
    # Run the test script using uv
    subprocess.run(['uv', 'run', 'test_mcp.py'], check=True)
    
    print("MCP server test completed successfully!")

def main():
    try:
        setup_environment()
        test_mcp()
        
        print("\nDone! MCP server is ready for Claude Desktop.")
        print("Copy the claude_desktop_config.json file to your Claude Desktop configuration directory.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Command failed with return code {e.returncode}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
