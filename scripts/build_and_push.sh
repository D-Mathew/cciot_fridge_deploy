#!/bin/bash

# Exitt immediately if a command exits with a non-zero status
set -e

# Define Docker repository (update with your Docker Hub or private registry)
DOCKER_REPO="dmathewtoh"

# Build and push Spoonacular image
echo "Building and pushing LLM1 Docker image..."
docker build -t $DOCKER_REPO/spoonacular-app:latest ../images/spoonacular-app
docker push $DOCKER_REPO/spoonacular-app:latest

# Build and push Whisper image
echo "Building and pushing LLM2 Docker image..."
docker build -t $DOCKER_REPO/whisper-app:latest ../images/whisper-app
docker push $DOCKER_REPO/whisper-app:latest

# Build and push ElevenLabs image
docker build -t $DOCKER_REPO/elevenlabs-app:latest ../images/elevenlabs-app
docker push $DOCKER_REPO/elevenlabs-app:latest

echo "All Docker images built and pushed successfully!"
