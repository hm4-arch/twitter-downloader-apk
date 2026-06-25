from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route("/download", methods=["POST"])
def download():

    try:

        data = request.get_json()

        url = data["url"]

        subprocess.run([
            "gallery-dl",
            "--cookies",
            "/storage/emulated/0/Download/cookies.txt",
            url
        ])

        return "Descarga finalizada"

    except Exception as e:

        return str(e), 500


app.run(
host="127.0.0.1",
port=5000
)
