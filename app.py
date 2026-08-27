from flask import Flask, jsonify
import os
if os.getenv("APPLICATIONINSIGHTS_CONNECTION_STRING"):
    from azure.monitor.opentelemetry import configure_azure_monitor
    configure_azure_monitor()

import pyodbc

app = Flask(__name__)


def get_db_connection():
    return pyodbc.connect(
        "DRIVER={ODBC Driver 18 for SQL Server};"
        f"SERVER={os.environ['DB_SERVER']};"
        f"DATABASE={os.environ['DB_NAME']};"
        f"UID={os.environ['DB_USER']};"
        f"PWD={os.environ['DB_PASSWORD']};"
        "Encrypt=yes;"
        "TrustServerCertificate=no;"
        "Connection Timeout=30;"
    )


@app.route("/")
def home():
    return "<h1>Contoso Retail Production - Cloud Migration </h1><p>Application deployed successfully</p>"


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": "contoso",
        "version": "1.0"
    }, 200


@app.route("/products")
def products():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT Id, Name, Price, Stock FROM Products")
    rows = cursor.fetchall()

    products = [
        {
            "id": row.Id,
            "name": row.Name,
            "price": float(row.Price),
            "stock": row.Stock
        }
        for row in rows
    ]

    cursor.close()
    conn.close()

    return jsonify(products)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
