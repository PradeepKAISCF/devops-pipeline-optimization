from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps CI/CD Pipeline Optimization Project"

@app.route("/health")
def health():
    return {"status": "pipeline running"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)