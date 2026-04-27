from flask import Flask, render_template, request, jsonify, abort
from automatas import afd1_bancario, afd2_cerradura, afd3_logistica
from automatas import afnd1_ids, afnd2_bioinformatica, afnd3_ecommerce

app = Flask(__name__)

# Registro central de todos los autómatas
AUTOMATAS = {
    "afd1": afd1_bancario,
    "afd2": afd2_cerradura,
    "afd3": afd3_logistica,
    "afnd1": afnd1_ids,
    "afnd2": afnd2_bioinformatica,
    "afnd3": afnd3_ecommerce,
}

# Metadatos para las tarjetas de la pantalla principal
METADATOS = {
    "afd1":  { "tipo": "afd",  "num": "AFD #1",  "titulo": "Flujo de Transacciones Bancarias",      "desc": "Valida que una transacción pase por: Autorización → Captura → Liquidación." },
    "afd2":  { "tipo": "afd",  "num": "AFD #2",  "titulo": "Cerradura Inteligente IoT",             "desc": "Bloquea el sistema tras 3 intentos fallidos consecutivos." },
    "afd3":  { "tipo": "afd",  "num": "AFD #3",  "titulo": "Orquestación de Pedidos Logísticos",    "desc": "Valida la secuencia de estados de un paquete logístico." },
    "afnd1": { "tipo": "afnd", "num": "AFND #1", "titulo": "validar_slack",      "desc": "Detecta si un mensaje está dirigido al bot y contiene un comando." },
    "afnd2": { "tipo": "afnd", "num": "AFND #2", "titulo": "analizar_proteina",  "desc": "Busca el patrón KGF en una secuencia de aminoácidos." },
    "afnd3": { "tipo": "afnd", "num": "AFND #3", "titulo": "analizar_comportamiento",   "desc": "Modela el comportamiento ambiguo de navegación de Home a Checkout." },
}


# ── Pantalla principal ──────────────────────────────────────────────
@app.route("/")
def index():
    return render_template("index.html", metadatos=METADATOS)


# ── Vista de detalle de un autómata ────────────────────────────────
@app.route("/automata/<string:auto_id>")
def detalle(auto_id):
    if auto_id not in AUTOMATAS:
        abort(404)
    modulo = AUTOMATAS[auto_id]
    definicion = modulo.obtener_definicion_formal()
    meta = METADATOS[auto_id]
    return render_template("detalle.html", definicion=definicion, meta=meta, auto_id=auto_id)


# ── API: validar cadena ─────────────────────────────────────────────
@app.route("/api/<string:auto_id>/validar", methods=["POST"])
def validar(auto_id):
    if auto_id not in AUTOMATAS:
        abort(404)
    datos = request.get_json()
    cadena = datos.get("cadena", "").strip()
    if not cadena:
        return jsonify({"error": "La cadena no puede estar vacía"}), 400
    resultado = AUTOMATAS[auto_id].procesar_cadena(cadena)
    return jsonify(resultado)


# ── API: definición formal ──────────────────────────────────────────
@app.route("/api/<string:auto_id>/definicion")
def definicion(auto_id):
    if auto_id not in AUTOMATAS:
        abort(404)
    return jsonify(AUTOMATAS[auto_id].obtener_definicion_formal())


if __name__ == "__main__":
    app.run(debug=True, port=5000)   # UN solo puerto