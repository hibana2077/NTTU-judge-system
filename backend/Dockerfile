FROM ubuntu:22.10

SHELL ["/bin/bash", "-c"]

WORKDIR /app

COPY . .

RUN sh ./install_all.sh

RUN pip3 install -r requirements.txt

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
RUN source "$HOME/.cargo/env"

RUN apt-get install -y time

EXPOSE 8000
EXPOSE 8080

CMD ["python3", "apiServer.py"]
# streamlit run dashboard.py --server.port 8080 --server.address 0.0.0.0
# CMD ["sh", "-c", "pwd; tail -f /dev/null"]