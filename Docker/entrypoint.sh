#!/usr/bin/env bash

# Entry point script for Docker Compose deployment workflow.
#
# Functionality:
#   - Change directory to the repository on the remote server.
#   - Fetch the latest changes from the origin.
#   - Reset the repository to the commit that triggered the workflow.
#   - Bring up Docker Compose services in detached mode.



git config --global --add safe.directory /home/docker

# Fetch the latest changes from the origin.
git fetch origin

# Reset the repository to the commit that triggered the workflow.
git reset --hard "${GITHUB_SHA}"

# python manage.py migrate

# Run Docker Compose in detached mode to deploy services.
python manage.py runserver 0.0.0.0:8000
