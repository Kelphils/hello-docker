# !/usr/bin/env bash

# create venv
python3 -m venv ~/.hello

# activate the environment
source ~/.hello/bin/activate

# Build Image
docker build --tag=my-running-app . / or
docker build -t my-running-app .

# List docker images
docker image ls

# Run flask app
docker run -p 8080:6001 my-running-app