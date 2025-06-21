from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Finanzas Brillantes – Módulo 1 activo"
