FROM python:3.8-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ src/
COPY .env .

# Create non-root user
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# Run the application
CMD ["python", "-m", "dockifyfm"] 