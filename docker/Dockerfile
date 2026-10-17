# TODO: нужно будет завендорить
FROM python:3.12-slim

RUN pip install uv

WORKDIR /app
COPY pyproject.toml uv.lock ./
COPY src/surveys/ .
RUN uv sync


CMD ["uv", "run", "uvicorn", "surveys.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--reload"]