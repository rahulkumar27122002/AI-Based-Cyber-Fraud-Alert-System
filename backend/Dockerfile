# backend/Dockerfile
FROM python:3.9-slim

# Create app directory
WORKDIR /app

# Avoid buffering stdout (useful for logs)
ENV PYTHONUNBUFFERED=1

# Copy requirements first for Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port used by Uvicorn
EXPOSE 8000

# Run the app
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
