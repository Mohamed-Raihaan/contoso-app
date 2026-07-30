from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Contoso Retail</h1><p>Application deployed successfully!</p>"

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
