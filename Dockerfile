FROM python:3.10-slim

WORKDIR /code

ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN apt update && apt install tesseract-ocr -y

RUN pip install -r requirements.txt

COPY . /code/

CMD ["python", "main.py"]