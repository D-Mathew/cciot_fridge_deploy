#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Deploy secrets
echo "Applying secrets for Elevenlabs..."
kubectl apply -f ../deployments/secrets/elevenlabs-secret.yaml

echo "Applying secrets for LLM2..."
kubectl apply -f ../deployments/secrets/spoonacular-secret.yaml

# Deploy Spoonacular
echo "Deploying Spoonacular Model"
kubectl apply -f ../deployments/spoonacular-deployment.yaml
kubectl apply -f ../deployments/services/spoonacular-service.yaml

# Deploy ElevenLabs TTS
echo "Deploying Elevenlabs Model"
kubectl apply -f ../deployments/elevenlabs-deployment.yaml
kubectl apply -f ../deployments/services/elevenlabs-service.yaml

# Deploy OpenAi-Whisper
echo "Deploying OpenAi Whisper"
kubectl apply -f ../deployments/whisper-deployment.yaml
kubectl apply -f ../deployments/services/whisper-service.yaml


echo "All resources deployed successfully!"