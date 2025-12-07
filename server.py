from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

# From Render Environment Variable
COZE_PAT = os.getenv("COZE_PAT")
COZE_TOKEN_URL = "https://api.coze.com/open_api/auth/token"

@app.route("/coze_token", methods=["GET"])
def get_token():
    if not COZE_PAT:
        return jsonify({"error": "COZE_PAT not found"}), 500

    resp = requests.post(
        COZE_TOKEN_URL,
        headers={"Authorization": f"Bearer {COZE_PAT}"}
    )

    if resp.status_code != 200:
        return jsonify({
            "error": "Coze API failed",
            "detail": resp.text
        }), 500

    data = resp.json()
    return jsonify({"token": data.get("access_token")})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
