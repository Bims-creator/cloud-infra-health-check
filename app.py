import os
import socket
from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.environ.get("APP_VERSION", "0.1.0")


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/version")
def version():
    return jsonify(version=APP_VERSION)


@app.route("/info")
def info():
    return jsonify(
        hostname=socket.gethostname(),
        version=APP_VERSION,
        timestamp=datetime.now(timezone.utc).isoformat(),
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
