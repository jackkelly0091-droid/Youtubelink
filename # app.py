app.py
from flask import Flask, request, send_file, jsonify
from pytube import YouTube
import os

app = Flask(__name__)
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

@app.route("/download", methods=["POST"])
def download_video():
    try:
        data = request.json
        url = data.get("url")
        if not url:
            return jsonify({"error": "No URL provided"}), 400

        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        filepath = stream.download(output_path=DOWNLOAD_FOLDER)

        return send_file(filepath, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

