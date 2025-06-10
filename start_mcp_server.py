#!/usr/bin/env python3

import os
import subprocess
import sys

def start_mcp_server():
    """Start the MCP server using uv"""
    # Set the working directory
    project_dir = '/Users/namirasuniaprita/Documents/GitHub/polyglot-mcp/polyglot-mcp'
    os.chdir(project_dir)
    
    # Run the server using uv
    try:
        # Using subprocess.run with check=True will raise an exception if the command fails
        subprocess.run(['uv', 'run', 'polyglot/server_fixed.py'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Server failed to start with return code {e.returncode}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    start_mcp_server()
