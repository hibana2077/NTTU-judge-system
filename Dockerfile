
# For more information, please refer to https://aka.ms/vscode-docker-python
FROM alpine:3.17.2

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# apt-get update
RUN apt-get install -y -q \
    build-essential \
    curl

# Install python
RUN apt-get install -y python3 python3-pip
RUN pip3 install --upgrade pip

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Install nodejs
RUN apt-get install -y nodejs npm
# Install VUE
RUN npm install vue
RUN npm install -g @vue/cli

# Install Ruby
RUN apt-get install ruby-full

# Install Rust



WORKDIR /app
COPY . /app

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["python", "frontend\client.py"]
