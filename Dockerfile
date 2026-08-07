
FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip

RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

CMD ["python", "main.py"]

