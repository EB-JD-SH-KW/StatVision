#!/usr/bin/env bash

# Entry point script for Docker Compose deployment workflow.
#
# Functionality:
#   - Change directory to the repository on the remote server.
#   - Fetch the latest changes from the origin.
#   - Reset the repository to the commit that triggered the workflow.
#   - Bring up Docker Compose services in detached mode.


# Fetch the latest changes from the origin.
git fetch origin

# Reset the repository to the commit that triggered the workflow.
# This assumes that the environment variable GITHUB_SHA is set.
git reset --hard "${GITHUB_SHA}"