from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Contoso retail Production - Cloud Engineer Arc </h1><p>Application deployed successfully By RAVEN</p>"
@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": "contoso",
        "version": "1.0"
    }, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
