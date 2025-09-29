FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

# All environment variables in one layer
ENV UV_SYSTEM_PYTHON=1 UV_COMPILE_BYTECODE=1 PYTHONUNBUFFERED=1 \
    DOCKER_CONTAINER=1



COPY requirements.txt requirements.txt




RUN uv pip install -r requirements.txt

EXPOSE 8080 8000

# Copy entire project

COPY . .


# Use the full module path

CMD ["python", "-m", "math_mcp"]
