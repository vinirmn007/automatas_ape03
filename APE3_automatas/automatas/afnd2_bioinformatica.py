"""
AFND - Análisis de Secuencias Bioinformáticas
Coincidente con: image_a91e0c.png
"""

ESTADOS = ["q0", "q1", "q2", "q3"]
ALFABETO = ["K", "G", "X", "F"]
ESTADO_INICIAL = "q0"
ESTADOS_ACEPTACION = {"q3"}

NOMBRES_ESTADOS = {
    "q0": "BÚSQUEDA_LISINA",
    "q1": "K_DETECTADA",
    "q2": "KG_EN_PROGRESO",
    "q3": "SECUENCIA_KGF_EXITO"
}

TABLA_TRANSICIONES = {
    "q0": {"K": ["q1", "q0"], "G": ["q0"], "X": ["q0"], "F": ["q0"]},
    "q1": {"K": [], "G": ["q2"], "X": [], "F": []},
    "q2": {"K": ["q2"], "G": ["q2"], "X": ["q2"], "F": ["q3", "q2"]},
    "q3": {"K": [], "G": [], "X": [], "F": []}
}

DESCRIPCION_SIMBOLOS = {
    "K": "Lisina (K)",
    "G": "Glicina (G)",
    "X": "Cualquier aminoácido",
    "F": "Fenilalanina (F)"
}

def clausura_epsilon(estados):
    return set(estados) # No hay lambdas en este modelo

def procesar_cadena(cadena: str) -> dict:
    cadena = cadena.upper().strip()
    estados_activos = clausura_epsilon({ESTADO_INICIAL})
    historial = [{"paso": 0, "simbolo": None, "estado_actual": sorted(list(estados_activos))}]

    for i, simbolo in enumerate(cadena, start=1):
        # Mapeo a X si no es un aminoácido del patrón principal
        simbolo_efectivo = simbolo if simbolo in ["K", "G", "F"] else "X"
        
        nuevos_estados = set()
        for estado in estados_activos:
            transiciones = TABLA_TRANSICIONES[estado].get(simbolo_efectivo, [])
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
        "patron": "KGX*F",
        "descripcion": "AFND que busca la secuencia proteica Lisina-Glicina-Cualquiera-Fenilalanina."
    }