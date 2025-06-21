from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "✅ Módulo 1 – Ganancias ejecutado desde Cloud Run correctamente."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Puerto que Cloud Run requiere
    app.run(host="0.0.0.0", port=port)        # Cloud Run exige host 0.0.0.0
