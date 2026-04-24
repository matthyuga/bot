from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/health")
def health():
    return {"ok": True, "service": "assistant-mvp"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
