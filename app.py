from flask import Flask, request, send_file
from datetime import datetime
import os

app = Flask(__name__)

LOG_FILE = "registros.csv"

@app.route("/pixel")
def pixel():
    pixel_id = request.args.get("id", "sin_id")
    ip = request.remote_addr
    agente = request.headers.get("User-Agent", "")
    hora = datetime.now().isoformat()

    # Guardamos el registro en un archivo .csv
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{hora},{pixel_id},{ip},{agente}\n")

    # Enviar imagen de 1x1 transparente
    return send_file("pixel.png", mimetype="image/png")

@app.route("/logs")
def mostrar_logs():
    try:
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            contenido = f.read()
    except FileNotFoundError:
        contenido = "Aún no hay registros."

    return f"<pre>{contenido}</pre>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
