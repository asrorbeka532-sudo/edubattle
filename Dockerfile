FROM python:3.11-slim

# System packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Set environment
ENV PORT=8000
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

# Start FastAPI backend with integrated Telegram Bot long-polling
CMD ["sh", "-c", "python -m uvicorn backend.app:app --host 0.0.0.0 --port ${PORT:-8000}"]
