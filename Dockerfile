FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# MCP servers communicate via stdio by default, so we don't need to expose ports
# unless we switch to SSE. For now, we use stdio.
ENTRYPOINT ["python", "server.py"]
