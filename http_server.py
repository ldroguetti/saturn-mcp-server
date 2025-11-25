from server import mcp

# Create a Streamable HTTP app
# This exposes the MCP server over HTTP with streaming capabilities
app = mcp.streamable_http_app()
