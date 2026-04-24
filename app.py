from flask import Flask, jsonify, render_template, request

from orchestrator import handle_turn

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/health")
def health():
    return {"ok": True, "service": "assistant-mvp"}


@app.post("/chat")
def chat():
    payload = request.get_json(silent=True) or {}
    user_input = str(payload.get("message", "")).strip()
    result = handle_turn(user_input)
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
