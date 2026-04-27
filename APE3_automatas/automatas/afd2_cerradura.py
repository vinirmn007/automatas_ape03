"""
AFD - Sistema de Seguridad IoT (Cerradura Inteligente)
Patrón: (C+FC+FFC)*+(C+F)*FFF(C+F)*
Alfabeto: {C, F}
Estados: {q0, q1, q2, q3}
Estado inicial: q0
Estado(s) de aceptación: {q0, q1, q2}  — q3 = bloqueado (trampa)
"""

ESTADOS = ["q0", "q1", "q2", "q3"]
ALFABETO = ["C", "F"]
ESTADO_INICIAL = "q0"
ESTADOS_ACEPTACION = {"q0", "q1", "q2"}   # q3 es estado de bloqueo
ESTADO_BLOQUEADO = "q3"

NOMBRES_ESTADOS = {
    "q0": "SIN FALLOS",
    "q1": "1 FALLO",
    "q2": "2 FALLOS",
    "q3": "BLOQUEADO",
}

TABLA_TRANSICIONES = {
    "q0": {"C": "q0", "F": "q1"},
    "q1": {"C": "q0", "F": "q2"},
    "q2": {"C": "q0", "F": "q3"},
    "q3": {"C": "q3", "F": "q3"},
}

DESCRIPCION_SIMBOLOS = {
    "C": "Correcto (acceso concedido)",
    "F": "Fallido (intento incorrecto)",
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
            "bloqueado": False,
        }
    ]

    for i, simbolo in enumerate(cadena, start=1):
        if simbolo not in ALFABETO:
            return {
                "aceptada": False,
                "estado_final": estado_actual,
                "nombre_estado_final": NOMBRES_ESTADOS[estado_actual],
                "historial": historial,
                "bloqueado": estado_actual == ESTADO_BLOQUEADO,
                "error": f"Símbolo '{simbolo}' no pertenece al alfabeto {ALFABETO}",
            }

        estado_anterior = estado_actual
        estado_actual = TABLA_TRANSICIONES[estado_actual][simbolo]
        bloqueado_ahora = estado_actual == ESTADO_BLOQUEADO

        historial.append(
            {
                "paso": i,
                "simbolo": simbolo,
                "descripcion": DESCRIPCION_SIMBOLOS[simbolo],
                "estado_anterior": estado_anterior,
                "nombre_estado_anterior": NOMBRES_ESTADOS[estado_anterior],
                "estado_actual": estado_actual,
                "nombre_estado": NOMBRES_ESTADOS[estado_actual],
                "bloqueado": bloqueado_ahora,
            }
        )

    aceptada = estado_actual in ESTADOS_ACEPTACION
    return {
        "aceptada": aceptada,
        "estado_final": estado_actual,
        "nombre_estado_final": NOMBRES_ESTADOS[estado_actual],
        "historial": historial,
        "bloqueado": estado_actual == ESTADO_BLOQUEADO,
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
        "estado_bloqueado": ESTADO_BLOQUEADO,
        "tabla_transiciones": TABLA_TRANSICIONES,
        "patron": "(C+FC+FFC)*+(C+F)*FFF(C+F)*",
        "descripcion": "Cerradura inteligente que bloquea tras 3 intentos fallidos consecutivos",
    }
