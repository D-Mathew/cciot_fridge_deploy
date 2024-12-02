#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Deploy secrets
echo "Deleting secrets for Elevenlabs..."
kubectl delete secret elevenlabs-secret

echo "Deleting secrets for Spoonacular..."
kubectl delete secret spoonacular-secret

# Deploy Spoonacular
echo "Deleting Spoonacular Model"
kubectl delete deploy spoonacular-app
kubectl delete service spoonacular-app-service

# Deploy ElevenLabs TTS
echo "Deleting Elevenlabs Model"
kubectl delete deploy elevenlabs-app
kubectl delete service elevenlabs-app-service

# Deploy OpenAi-Whisper
echo "Deleting OpenAi Whisper"
kubectl delete deploy whisper-app
kubectl delete service whisper-app-service


echo "All resources deleted successfully!"
