FROM ubuntu:22.10

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip

RUN apt-get install -y iputils-ping

RUN pip3 install --upgrade pip

RUN apt-get install -y curl

RUN pip3 install fastapi uvicorn

EXPOSE 8000

WORKDIR /app
COPY . /app

CMD ["python3", "api.py"]