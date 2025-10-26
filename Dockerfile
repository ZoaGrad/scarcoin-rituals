FROM python:3.11-slim as builder

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Runtime stage
FROM python:3.11-slim

WORKDIR /app

# Copy Python dependencies from builder
COPY --from=builder /usr/local/lib/python3.11/site-packages/ /usr/local/lib/python3.11/site-packages/
COPY --from=builder /usr/local/bin/ /usr/local/bin/

# Create non-root user
RUN groupadd -r scarcoin && useradd -r -g scarcoin scarcoin

# Copy application code
COPY core/ ./core/
COPY governance/ ./governance/
COPY integration/ ./integration/
COPY oracle/ ./oracle/
COPY tests/ ./tests/

# Create necessary directories and set permissions
RUN mkdir -p /app/logs /app/data && \
    chown -R scarcoin:scarcoin /app

USER scarcoin

EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

CMD ["uvicorn", "oracle.scarindex_service:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]