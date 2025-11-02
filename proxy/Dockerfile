FROM python:3.11-slim

WORKDIR /app
COPY proxy_server.py .

RUN pip install fastapi uvicorn httpx python-dotenv

EXPOSE 8080
CMD ["uvicorn", "proxy_server:app", "--host", "0.0.0.0", "--port", "8080"]
