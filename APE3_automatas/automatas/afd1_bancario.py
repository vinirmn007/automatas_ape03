"""
AFD - Validador de Flujo de Transacciones Bancarias
Patrón: ACL
Alfabeto: {A, C, L}
Estados: {q0, q1, q2, q3, q4}
Estado inicial: q0
Estado(s) de aceptación: {q3}
"""

ESTADOS = ["q0", "q1", "q2", "q3", "q4"]
ALFABETO = ["A", "C", "L"]
ESTADO_INICIAL = "q0"
ESTADOS_ACEPTACION = {"q3"}

NOMBRES_ESTADOS = {
    "q0": "INICIADA",
    "q1": "AUTORIZADA",
    "q2": "CAPTURADA",
    "q3": "COMPLETADA/LIQUIDADA",
    "q4": "ERROR",
}

TABLA_TRANSICIONES = {
    "q0": {"A": "q1", "C": "q4", "L": "q4"},
    "q1": {"A": "q4", "C": "q2", "L": "q4"},
    "q2": {"A": "q4", "C": "q4", "L": "q3"},
    "q3": {"A": "q4", "C": "q4", "L": "q4"},
    "q4": {"A": "q4", "C": "q4", "L": "q4"},
}

DESCRIPCION_SIMBOLOS = {
    "A": "Autorizar",
    "C": "Capturar",
    "L": "Liquidar",
}


def procesar_cadena(cadena: str) -> dict:
    """
    Procesa una cadena de entrada y retorna el resultado del AFD.
    Retorna un dict con: estado_final, aceptada, historial de pasos.
    """
    cadena = cadena.upper().strip()
    estado_actual = ESTADO_INICIAL
    historial = [
        {
            "paso": 0,
            "simbolo": None,
            "estado_anterior": None,
            "estado_actual": estado_actual,
            "nombre_estado": NOMBRES_ESTADOS[estado_actual],
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
        estado_actual = TABLA_TRANSICIONES[estado_actual][simbolo]

        historial.append(
            {
                "paso": i,
                "simbolo": simbolo,
                "descripcion": DESCRIPCION_SIMBOLOS[simbolo],
                "estado_anterior": estado_anterior,
                "nombre_estado_anterior": NOMBRES_ESTADOS[estado_anterior],
                "estado_actual": estado_actual,
                "nombre_estado": NOMBRES_ESTADOS[estado_actual],
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
    return {
        "estados": ESTADOS,
        "nombres_estados": NOMBRES_ESTADOS,
        "alfabeto": ALFABETO,
        "descripcion_simbolos": DESCRIPCION_SIMBOLOS,
        "estado_inicial": ESTADO_INICIAL,
        "estados_aceptacion": list(ESTADOS_ACEPTACION),
        "tabla_transiciones": TABLA_TRANSICIONES,
        "patron": "ACL",
        "descripcion": "Valida que una transacción bancaria pase por: Autorización → Captura → Liquidación",
    }
