# Set an environment variable to prevent Python from buffering stdout/stderr.
# Start with a minimal Python 3.12 image. (slim version for smaller size).
FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    libmariadb-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set an environment variable to prevent Python from buffering stdout/stderr.
ENV PYTHONUNBUFFERED=1

# Install nessecary packages
RUN apt update && apt install -y \
    git \
    default-libmysqlclient-dev \
    libmariadb-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container.
WORKDIR /app

# Copy the requirements file from the host system to the container's working directory.
COPY requirements.txt requirements.txt

# Use pip to install the dependencies listed in the requirements file.
RUN python -m  pip install --no-cache-dir --requirement requirements.txt
