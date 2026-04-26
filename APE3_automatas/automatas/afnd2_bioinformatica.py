"""
AFND - Reconocimiento de Secuencias Genéticas (Bioinformática)
Patrón: K G X* F
Alfabeto: {K, G, X, F}
Estados: {q0, q1, q2, q3}
Estado inicial: q0
Estado(s) de aceptación: {q3}

Tabla de transiciones (AFND):
     K          G     X          F
q0: {q1,q0}   q0    q0         q0
q1: -          q2    -          -
q2: q2         q2    q2         {q3,q2}
q3: -          -     -          -
"""

ESTADOS = ["q0", "q1", "q2", "q3"]
ALFABETO = ["K", "G", "X", "F"]
ESTADO_INICIAL = "q0"
ESTADOS_ACEPTACION = {"q3"}

NOMBRES_ESTADOS = {
    "q0": "BUSQUEDA",
    "q1": "K_ENCONTRADA",
    "q2": "KG_ENCONTRADO",
    "q3": "SECUENCIA_HALLADA",
}

TABLA_TRANSICIONES = {
    "q0": {"K": ["q1", "q0"], "G": ["q0"], "X": ["q0"], "F": ["q0"]},
    "q1": {"K": [],            "G": ["q2"], "X": [],      "F": []},
    "q2": {"K": ["q2"],        "G": ["q2"], "X": ["q2"],  "F": ["q3", "q2"]},
    "q3": {"K": [],            "G": [],     "X": [],       "F": []},
}

DESCRIPCION_SIMBOLOS = {
    "K": "Lysina",
    "G": "Glicina",
    "X": "Aminoácido genérico",
    "F": "Fenilalanina",
}


def epsilon_cierre(estados: set) -> set:
    return set(estados)


def mover(estados: set, simbolo: str) -> set:
    siguiente = set()
    for estado in estados:
        destinos = TABLA_TRANSICIONES.get(estado, {}).get(simbolo, [])
        siguiente.update(destinos)
    return siguiente


def procesar_cadena(cadena: str) -> dict:
    cadena = cadena.upper().strip()
    estados_actuales = epsilon_cierre({ESTADO_INICIAL})
    historial = [
        {
            "paso": 0,
            "simbolo": None,
            "estados_anteriores": None,
            "estados_actuales": list(estados_actuales),
            "nombres_estados": [NOMBRES_ESTADOS[e] for e in estados_actuales],
        }
    ]

    for i, simbolo in enumerate(cadena, start=1):
        if simbolo not in ALFABETO:
            return {
                "aceptada": False,
                "estados_finales": list(estados_actuales),
                "historial": historial,
                "error": f"Símbolo '{simbolo}' no pertenece al alfabeto {ALFABETO}",
            }

        estados_anteriores = estados_actuales
        estados_actuales = epsilon_cierre(mover(estados_actuales, simbolo))

        historial.append(
            {
                "paso": i,
                "simbolo": simbolo,
                "descripcion": DESCRIPCION_SIMBOLOS[simbolo],
                "estados_anteriores": list(estados_anteriores),
                "nombres_estados_anteriores": [NOMBRES_ESTADOS[e] for e in estados_anteriores],
                "estados_actuales": list(estados_actuales),
                "nombres_estados": [NOMBRES_ESTADOS[e] for e in estados_actuales],
                "muerto": len(estados_actuales) == 0,
            }
        )

        if not estados_actuales:
            return {
                "aceptada": False,
                "estados_finales": [],
                "historial": historial,
                "error": None,
            }

    aceptada = bool(estados_actuales & ESTADOS_ACEPTACION)
    return {
        "aceptada": aceptada,
        "estados_finales": list(estados_actuales),
        "nombres_estados_finales": [NOMBRES_ESTADOS[e] for e in estados_actuales],
        "historial": historial,
        "error": None,
    }


def obtener_definicion_formal() -> dict:
    return {
        "estados": ESTADOS,
        "nombres_estados": NOMBRES_ESTADOS,
        "alfabeto": ALFABETO,
        "descripcion_simbolos": DESCRIPCION_SIMBOLOS,
        "estado_inicial": ESTADO_INICIAL,
        "estados_aceptacion": list(ESTADOS_ACEPTACION),
        "tabla_transiciones": TABLA_TRANSICIONES,
        "patron": "K G X* F",
        "descripcion": "Reconoce la secuencia proteica: Lysina, Glicina, cualquier aminoácido*, Fenilalanina",
        "tipo": "AFND",
    }
