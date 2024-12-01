# cciot_fridge_deploy

## Setting Up
1. Run ```./scripts/build_and_push.sh``` to build the images. You need to change the Docker Repo Name in the file
2. Run ```./scripts/deploy_all.sh``` to apply all the required yaml files for the deployment 

## Example Usage of Models

### Spoonacular
```curl <ip>:<port>/?ingredients=tomato,cheese```

### OpenAi-Whisper
```curl -X POST <ip>:<port>/ -F "file=@<filename>"```

### ElevenLabs TTS
```curl -X POST <ip>:<port>/ -H "Content-Type: application/json" -d "{'text': 'Hello, Welcome to my application'}" -o output_audio.mp3```