FROM python:3.8.5

RUN pip install --upgrade pip

RUN pip install fastapi uvicorn numpy  opencv-python python-multipart pillow python-socketio requests aiofiles jsonschema



EXPOSE 8005

COPY . .

CMD ["uvicorn", "start:app", "--host", "0.0.0.0", "--port", "8005"]
