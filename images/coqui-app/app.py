from flask import Flask, request, jsonify, send_file
import json

app = Flask(__name__)

device = "cuda" if torch.cuda.is_available() else "cpu"
tts = TTS(model_name="tts_models/en/ljspeech/glow-tts").to(device)

@app.route('/', methods=['POST'])
def textToSpeech():
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = request.data.decode('utf-8')
            json_data = eval(data)
            text = json_data.get("text")

            tts.tts_to_file(text=text, file_path="output_audio.wav")            
            return send_file('output_audio.wav', as_attachment=True)
        else:
            return jsonify({"message": "Content-Type Not Supported"}), 406
    except Exception as err:
        return jsonify({'Error': f'{err}'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9002) 
