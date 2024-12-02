import requests
from elevenlabs import ElevenLabs
from flask import Flask, request, jsonify, send_file
import json
import os
import subprocess

app = Flask(__name__)
client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY", "").strip())
print(dir(client.generate))

@app.route('/', methods=['POST'])
def textToSpeech():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = request.data.decode('utf-8')
            json_data = eval(data)
            text = json_data.get("text")
            
            print(text)
            print(client)
            # Generate Audio
            audio = client.generate(
                    text=text,
                    voice="Rachel",
                    model="eleven_turbo_v2"
            )

            with open('output_audio.mp3', 'wb') as audiofile:
                for chunk in audio:
                    audiofile.write(chunk)
                    
            subprocess.run([
                "ffmpeg", "-i", "output_audio.mp3", "-ar", "44100", "-ac", "2", "-sample_fmt", "s16", "output_audio_44100Hz_16bit.wav"
            ])

            return send_file('output_audio_44100Hz_16bit.wav', as_attachment=True)
        else:
            return jsonify({"message": "Content-Type Not Supported"}), 406
    except Exception as err:
        return jsonify({'Error': f'{err}'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9002) 
