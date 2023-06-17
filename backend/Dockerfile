FROM ubuntu:22.04

SHELL ["/bin/bash", "-c"]

WORKDIR /app

COPY . .

RUN sh ./install_all.sh

RUN pip3 install -r requirements.txt

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
RUN source "$HOME/.cargo/env"

EXPOSE 8000
EXPOSE 8080

CMD ["python3", "apiServer.py"]
# streamlit run dashboard.py --server.port 8080
# CMD ["sh", "-c", "pwd; tail -f /dev/null"]