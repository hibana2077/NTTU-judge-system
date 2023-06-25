FROM ubuntu:22.10

SHELL ["/bin/bash", "-c"]

WORKDIR /app

COPY . .

RUN apt-get update
RUN apt-get install -y python3 python3-pip curl vim git wget gcc g++ nodejs golang-go ruby-full
RUN apt-get install -y time

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
RUN source "$HOME/.cargo/env"

RUN pip3 install -r requirements.txt

EXPOSE 8000
EXPOSE 8080

CMD ["python3", "apiServer.py"]
# streamlit run dashboard.py --server.port 8080 --server.address 0.0.0.0
# CMD ["sh", "-c", "pwd; tail -f /dev/null"]