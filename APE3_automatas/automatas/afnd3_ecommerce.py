"""
AFND - Sistema de Recomendación E-commerce
Coincidente con: image_a91dcd.png
"""

ESTADOS = ["q0", "q1", "q2", "q3"]
ALFABETO = ["H", "S", "C"]
ESTADO_INICIAL = "q0"
ESTADOS_ACEPTACION = {"q3"}

NOMBRES_ESTADOS = {
    "q0": "INICIO_SESION",
    "q1": "NAVEGANDO_HOME",
    "q2": "INTERÉS_BÚSQUEDA",
    "q3": "CONVERSIÓN_CARRITO"
}

TABLA_TRANSICIONES = {
    "q0": {"H": ["q1"], "S": [], "C": []},
    "q1": {"H": [], "S": ["q2", "q1"], "C": []},
    "q2": {"H": [], "S": [], "C": ["q3"]},
    "q3": {"H": [], "S": [], "C": []}
}

DESCRIPCION_SIMBOLOS = {
    "H": "Home (H)",
    "S": "Search (S)",
    "C": "Cart (C)"
}

def clausura_epsilon(estados):
    return set(estados)

def procesar_cadena(cadena: str) -> dict:
    cadena = cadena.upper().strip()
    estados_activos = clausura_epsilon({ESTADO_INICIAL})
    historial = [{"paso": 0, "simbolo": None, "estado_actual": sorted(list(estados_activos))}]

    for i, simbolo in enumerate(cadena, start=1):
        nuevos_estados = set()
        for estado in estados_activos:
            transiciones = TABLA_TRANSICIONES[estado].get(simbolo, [])
            for dest in transiciones:
                nuevos_estados.add(dest)
        
        estados_anteriores = estados_activos
        estados_activos = clausura_epsilon(nuevos_estados)
        
        historial.append({
            "paso": i,
            "simbolo": simbolo,
            "estado_anterior": sorted(list(estados_anteriores)),
            "estado_actual": sorted(list(estados_activos))
        })
            
    aceptada = any(e in ESTADOS_ACEPTACION for e in estados_activos)
    return {
        "aceptada": aceptada,
        "estado_final": sorted(list(estados_activos)),
        "historial": historial
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
        "patron": "HS+C",
        "descripcion": "AFND que modela el comportamiento del cliente desde Home hasta Checkout."
    }