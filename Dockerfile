FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && pip install .

EXPOSE 8000

CMD ["sh", "-c", "python -m uvicorn src.app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]
