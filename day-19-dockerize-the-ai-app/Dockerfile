FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY code ./code

EXPOSE 8000

CMD ["uvicorn", "code.api:app", "--host", "0.0.0.0", "--port", "8000"]
