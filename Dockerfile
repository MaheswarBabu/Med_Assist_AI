
# ==========================================
# Stage 1: Builder
# ==========================================
FROM python:3.11-slim AS builder

WORKDIR /app

# Create an isolated Python environment
RUN python -m venv /opt/venv

# Install dependencies
COPY requirements.txt .
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt


# ==========================================
# Stage 2: Runtime
# ==========================================
FROM python:3.11-slim AS runtime

WORKDIR /app

# Copy the installed environment from builder
COPY --from=builder /opt/venv /opt/venv

# Copy application source code
COPY backend/ ./backend/
COPY frontend/ ./frontend/

# Use the virtual environment
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONUNBUFFERED=1

# Gradio and FastAPI ports
EXPOSE 7860 8000

# Start backend and frontend
CMD ["sh", "-c", "uvicorn backend.main:app --host 0.0.0.0 --port 8000 & python frontend/app.py"]
