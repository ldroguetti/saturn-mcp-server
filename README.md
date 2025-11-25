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


### Dokploy (VPS)

1.  **Create an Application**:
    *   Log in to your Dokploy dashboard.
    *   Create a new "Application".
    *   Name it `saturn-mcp`.

2.  **Source Control**:
    *   Select "Git".
    *   Enter your repository URL.
    *   Select the branch (e.g., `main`).

3.  **Build Settings**:
    *   **Build Type**: Select `Dockerfile`.
    *   **Dockerfile Path**: `./Dockerfile`.
    *   **Context Path**: `./`.

4.  **Deploy**:
    *   Click "Deploy".
    *   Dokploy will build the image using the `Dockerfile` and start the service.

## Usage

### 1. Local (Stdio)

Add the following to your `claude_desktop_config.json`:

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

### 2. Remote / Docker (SSE)

If you have deployed the server using Docker (e.g., on Dokploy or locally), it exposes an SSE endpoint at `http://<your-server-ip>:8000/sse`.

Add the following to your `claude_desktop_config.json` (or Cursor settings):

```json
{
  "mcpServers": {
    "saturn-remote": {
      "command": "docker",
      "args": [],
      "url": "http://<your-server-ip>:8000/sse"
    }
  }
}
```

> **Note**: For Cursor, you can add the SSE URL directly in the "MCP Servers" settings.
