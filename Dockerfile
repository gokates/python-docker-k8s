# syntax=docker/dockerfile:1

FROM python:3.9-slim-buster
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "/app/source/app.py"]
CMD ["-e", "development", "--host", "0.0.0.0:5000"]
