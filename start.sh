#!/bin/bash

# Define variables
IMAGE_NAME="my-streamlit-jupyter-app"
CONTAINER_NAME="streamlit_jupyter_container"
HOST_PORT_STREAMLIT=8501
HOST_PORT_JUPYTER=8888
CONTAINER_PORT_STREAMLIT=8501
CONTAINER_PORT_JUPYTER=8888
APP_DIR="$(pwd -W)/app"  # Use pwd -W to get the Windows-style path of the current directory

# Check if the Dockerfile exists in the current directory
if [ ! -f "./Dockerfile" ]; then
    echo "Dockerfile not found in the current directory"
    exit 1
fi

# Build the Docker image
echo "Building Docker image..."
docker build -t $IMAGE_NAME .

# Check if the container is already running and stop it if necessary
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "Stopping existing container..."
    docker stop $CONTAINER_NAME
    docker rm $CONTAINER_NAME
fi

# Run the Docker container with the volume mount
echo "Running Docker container..."
docker run -d \
    --name $CONTAINER_NAME \
    -p $HOST_PORT_STREAMLIT:$CONTAINER_PORT_STREAMLIT \
    -p $HOST_PORT_JUPYTER:$CONTAINER_PORT_JUPYTER \
    -v "$APP_DIR:/app" \
    $IMAGE_NAME

echo "Container is running."
echo "Access Streamlit at http://localhost:$HOST_PORT_STREAMLIT"
echo "Access JupyterLab at http://localhost:$HOST_PORT_JUPYTER"
