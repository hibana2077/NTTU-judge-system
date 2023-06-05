FROM ubuntu:23.04

RUN apt update && apt install -y python3 python3-pip

WORKDIR /app

COPY . .

RUN sh ./install_all.sh

RUN pip3 install -r requirements.txt