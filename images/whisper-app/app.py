import whisper
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

model = whisper.load_model("tiny", device="cpu") # Need to change to a different device (Using this for my device)

@app.route('/', methods=['POST'])
def speechToText():
    try:
        if 'file' not in request.files:
            return jsonify({"error": "No file part in the request"}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({"error": "No file selected"}), 400

        # Save the uploaded file
        print(file.filename)
        file.save(f"./uploads/{file.filename}")
        result = model.transcribe(f"./uploads/{file.filename}")
        return jsonify({'text':result['text']})
    except Exception as err:
        return jsonify({'Error': f'{err}'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9001)
