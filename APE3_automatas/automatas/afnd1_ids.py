"""
AFND - Detección de Patrones de Ataque en Ciberseguridad (IDS)
Patrón: SYN ACK+ RST
Alfabeto: {SYN, ACK, RST}
Estados: {q0, q1, q2, q3}
Estado inicial: q0
Estado(s) de aceptación: {q3}

NOTA PARA EL DESARROLLADOR:
- Este es un AFND (Autómata Finito No Determinista)
- La función de transición retorna CONJUNTOS de estados: δ: Q × Σ → P(Q)
- Implementar el algoritmo de simulación por subconjuntos o seguimiento de todos
  los estados activos simultáneos
- TODO: Completar la tabla de transiciones según el problema
"""

ESTADOS = ["q0", "q1", "q2", "q3"]
ALFABETO = ["SYN", "ACK", "RST"]
ESTADO_INICIAL = "q0"
ESTADOS_ACEPTACION = {"q3"}

NOMBRES_ESTADOS = {
    "q0": "INICIO",
    "q1": "SYN_RECIBIDO",
    "q2": "ACK_RECIBIDO",
    "q3": "ATAQUE_DETECTADO",
}

# TODO: Completar/verificar la tabla de transiciones para el AFND
# Los valores son CONJUNTOS de estados (lista vacía = transición muerta)
TABLA_TRANSICIONES = {
    "q0": {"SYN": ["q1"], "ACK": [],        "RST": []},
    "q1": {"SYN": [],     "ACK": ["q2"],     "RST": []},
    "q2": {"SYN": [],     "ACK": ["q2"],     "RST": ["q3"]},
    "q3": {"SYN": [],     "ACK": [],         "RST": []},
}

DESCRIPCION_SIMBOLOS = {
    "SYN": "Intento de conexión",
    "ACK": "Respuesta del servidor",
    "RST": "Paquete de reset",
}


def epsilon_cierre(estados: set) -> set:
    """Calcula el ε-cierre de un conjunto de estados (no hay transiciones ε aquí)."""
    return set(estados)


def mover(estados: set, simbolo: str) -> set:
    """Retorna todos los estados alcanzables desde 'estados' con 'simbolo'."""
    siguiente = set()
    for estado in estados:
        destinos = TABLA_TRANSICIONES.get(estado, {}).get(simbolo, [])
        siguiente.update(destinos)
    return siguiente


def procesar_cadena(tokens: list) -> dict:
    """
    Procesa una lista de tokens (símbolos del alfabeto).
    Simula el AFND con seguimiento de todos los estados activos.
    """
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

    for i, simbolo in enumerate(tokens, start=1):
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
        "patron": "SYN ACK+ RST",
        "descripcion": "Detecta el patrón de ataque: SYN seguido de uno o más ACK y un RST final",
        "tipo": "AFND",
    }
