from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '✅ Módulo 1 – Ganancias funcionando desde Cloud Run'

if __name__ == '__main__':
    # 👇 Esto es crítico: escuchar en el puerto proporcionado por Cloud Run
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
