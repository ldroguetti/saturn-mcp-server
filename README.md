# Saturn MCP Server

An MCP server to search and read Rocketbot Saturn documentation.

## Features

- **Search**: Search for documentation articles.
- **Read**: Read the content of a specific documentation page.

## Installation

### Local

1.  Clone the repository.
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the server:
    ```bash
    python server.py
    ```

### Docker

1.  Build and run with Docker Compose:
    ```bash
    docker-compose up --build
    ```

## Usage with Claude Desktop

Add the following to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "saturn": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "saturn-mcp"
      ]
    }
  }
}
```

Or if running locally without Docker:

```json
{
  "mcpServers": {
    "saturn": {
      "command": "python",
      "args": [
        "/path/to/saturn-mcp-server/server.py"
      ]
    }
  }
}
```
