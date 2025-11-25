FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose port 8000 for SSE
EXPOSE 8000

# Run with uvicorn for SSE support
CMD ["uvicorn", "sse:app", "--host", "0.0.0.0", "--port", "8000"]
