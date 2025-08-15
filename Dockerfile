FROM python:3.12-slim

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies with cache mount for faster rebuilds
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project

# Copy application code
COPY main.py ./

# Install the project itself
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

# Set PATH to use the virtual environment
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 80

# Run with multiple workers for production
CMD ["fastapi", "run", "--workers", "4", "--host", "0.0.0.0", "--port", "80", "main.py"]