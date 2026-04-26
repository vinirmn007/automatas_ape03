"""
AFND - Sistema de Detección de Comandos (IDS)
Patrón: @bot [user] comando
Basado en: image_a91d95.png
"""

ESTADOS = ["q0", "q1", "q2", "q3"]
ALFABETO = ["B", "W", "C", "ε"] # B=@bot, W=Word/User, C=Command
ESTADO_INICIAL = "q0"
ESTADOS_ACEPTACION = {"q3"}

NOMBRES_ESTADOS = {
    "q0": "ESPERA_MENCION",
    "q1": "MENCION_DETECTADA",
    "q2": "ESPERA_COMANDO",
    "q3": "COMANDO_VALIDO"
}

TABLA_TRANSICIONES = {
    "q0": {"B": ["q1"], "W": [], "C": [], "ε": []},
    "q1": {"B": [], "W": ["q2"], "C": [], "ε": ["q2"]},
    "q2": {"B": [], "W": [], "C": ["q3"], "ε": []},
    "q3": {"B": [], "W": [], "C": [], "ε": []}
}

DESCRIPCION_SIMBOLOS = {
    "B": "@bot (Mención)",
    "W": "Usuario/Palabra",
    "C": "Comando (!cmd o ?help)",
    "ε": "Transición Lambda (Opcional)"
}

def clausura_epsilon(estados):
    clausura = set(estados)
    pila = list(estados)
    while pila:
        estado = pila.pop()
        for dest in TABLA_TRANSICIONES[estado].get("ε", []):
            if dest not in clausura:
                clausura.add(dest)
                pila.append(dest)
    return clausura

def procesar_cadena(cadena_tokens: list) -> dict:
    # Asumimos que los tokens ya vienen clasificados como B, W o C
    estados_activos = clausura_epsilon({ESTADO_INICIAL})
    historial = [{"paso": 0, "simbolo": None, "estado_actual": sorted(list(estados_activos))}]

    for i, simbolo in enumerate(cadena_tokens, start=1):
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

# ESTA ES LA FUNCIÓN QUE TE DABA EL ERROR
def obtener_definicion_formal() -> dict:
    return {
        "estados": ESTADOS,
        "nombres_estados": NOMBRES_ESTADOS,
        "alfabeto": ALFABETO,
        "descripcion_simbolos": DESCRIPCION_SIMBOLOS,
        "estado_inicial": ESTADO_INICIAL,
        "estados_aceptacion": list(ESTADOS_ACEPTACION),
        "tabla_transiciones": TABLA_TRANSICIONES,
        "patron": "@bot (USER)? (!cmd | ?help)",
        "descripcion": "AFND-λ que detecta comandos para un bot con usuario opcional."
    }