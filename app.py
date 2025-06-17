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