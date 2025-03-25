# Start with a minimal Python 3.12 image. (slim version for smaller size).
FROM python:3.12-slim

# Set an environment variable to prevent Python from buffering stdout/stderr.
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container.
WORKDIR /home/docker

# Copy the requirements file from the host system to the container's working directory.
COPY ../requirements.txt requirements.txt

# Use pip to install the dependencies listed in the requirements file.
RUN pip3 install -r requirements.txt
