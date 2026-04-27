"""
AFD - Orquestación de Pedidos de Logística
Patrón: CPE(T+D)+CPX
Alfabeto: {C, P, E, T, D, X}
Estados: {q0, q1, q2, q3, q4, q5, q6}
Estado inicial: q0
Estado(s) de aceptación: {q4, q5, q6}
"""

ESTADOS = ["q0", "q1", "q2", "q3", "q4", "q5", "q6"]
ALFABETO = ["C", "P", "E", "T", "D", "X"]
ESTADO_INICIAL = "q0"
ESTADOS_ACEPTACION = {"q4", "q5", "q6"}

NOMBRES_ESTADOS = {
    "q0": "INICIO",
    "q1": "CREADO",
    "q2": "EMPAQUETADO",
    "q3": "ENVIADO",
    "q4": "ENTREGADO",
    "q5": "DEVUELTO",
    "q6": "CANCELADO",
}

# "-" representa transición inválida (estado de trampa no explícito)
TABLA_TRANSICIONES = {
    "q0": {"C": "q1",  "P": None, "E": None, "T": None, "D": None, "X": None},
    "q1": {"C": None,  "P": "q2", "E": None, "T": None, "D": None, "X": "q6"},
    "q2": {"C": None,  "P": None, "E": "q3", "T": None, "D": None, "X": "q6"},
    "q3": {"C": None,  "P": None, "E": None, "T": "q4", "D": "q5", "X": None},
    "q4": {"C": None,  "P": None, "E": None, "T": None, "D": "q5", "X": None},
    "q5": {"C": None,  "P": None, "E": None, "T": None, "D": None, "X": None},
    "q6": {"C": None,  "P": None, "E": None, "T": None, "D": None, "X": None},
}

DESCRIPCION_SIMBOLOS = {
    "C": "Creado",
    "P": "Empaquetado",
    "E": "Enviado",
    "T": "Entregado",
    "D": "Devuelto",
    "X": "Cancelado",
}


def procesar_cadena(cadena: str) -> dict:
    cadena = cadena.upper().strip()
    estado_actual = ESTADO_INICIAL
    historial = [
        {
            "paso": 0,
            "simbolo": None,
            "estado_anterior": None,
            "estado_actual": estado_actual,
            "nombre_estado": NOMBRES_ESTADOS[estado_actual],
            "transicion_invalida": False,
        }
    ]

    for i, simbolo in enumerate(cadena, start=1):
        if simbolo not in ALFABETO:
            return {
                "aceptada": False,
                "estado_final": estado_actual,
                "nombre_estado_final": NOMBRES_ESTADOS[estado_actual],
                "historial": historial,
                "error": f"Símbolo '{simbolo}' no pertenece al alfabeto {ALFABETO}",
            }

        estado_anterior = estado_actual
        siguiente = TABLA_TRANSICIONES[estado_actual][simbolo]
        transicion_invalida = siguiente is None

        if transicion_invalida:
            historial.append(
                {
                    "paso": i,
                    "simbolo": simbolo,
                    "descripcion": DESCRIPCION_SIMBOLOS[simbolo],
                    "estado_anterior": estado_anterior,
                    "nombre_estado_anterior": NOMBRES_ESTADOS[estado_anterior],
                    "estado_actual": estado_anterior,
                    "nombre_estado": NOMBRES_ESTADOS[estado_anterior],
                    "transicion_invalida": True,
                }
            )
            return {
                "aceptada": False,
                "estado_final": estado_anterior,
                "nombre_estado_final": NOMBRES_ESTADOS[estado_anterior],
                "historial": historial,
                "error": f"Transición inválida: no se puede '{DESCRIPCION_SIMBOLOS[simbolo]}' desde '{NOMBRES_ESTADOS[estado_anterior]}'",
            }

        estado_actual = siguiente
        historial.append(
            {
                "paso": i,
                "simbolo": simbolo,
                "descripcion": DESCRIPCION_SIMBOLOS[simbolo],
                "estado_anterior": estado_anterior,
                "nombre_estado_anterior": NOMBRES_ESTADOS[estado_anterior],
                "estado_actual": estado_actual,
                "nombre_estado": NOMBRES_ESTADOS[estado_actual],
                "transicion_invalida": False,
            }
        )

    aceptada = estado_actual in ESTADOS_ACEPTACION
    return {
        "aceptada": aceptada,
        "estado_final": estado_actual,
        "nombre_estado_final": NOMBRES_ESTADOS[estado_actual],
        "historial": historial,
        "error": None,
    }


def obtener_definicion_formal() -> dict:
    # Convertir None a "-" para el front
    tabla_display = {}
    for estado, trans in TABLA_TRANSICIONES.items():
        tabla_display[estado] = {
            s: (v if v is not None else "-") for s, v in trans.items()
        }
    return {
        "estados": ESTADOS,
        "nombres_estados": NOMBRES_ESTADOS,
        "alfabeto": ALFABETO,
        "descripcion_simbolos": DESCRIPCION_SIMBOLOS,
        "estado_inicial": ESTADO_INICIAL,
        "estados_aceptacion": list(ESTADOS_ACEPTACION),
        "tabla_transiciones": tabla_display,
        "patron": "CPE(T+D)+CPX",
        "descripcion": "Valida la secuencia de estados de un paquete logístico",
    }
