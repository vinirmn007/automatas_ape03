ESTADOS = ["q0", "q1", "q2", "q3"]
ALFABETO = ["bot", "user", "cmd", "help", "epsilon"]
ESTADO_INICIAL = "q0"
ESTADOS_ACEPTACION = {"q3"}

NOMBRES_ESTADOS = {
    "q0": "ESPERA_MENCION",
    "q1": "MENCION_DETECTADA",
    "q2": "ESPERA_COMANDO",
    "q3": "COMANDO_VALIDO"
}

TABLA_TRANSICIONES = {
    "q0": {"bot": ["q1"], "user": [], "cmd": [], "help": [], "epsilon": []},
    "q1": {"bot": [], "user": ["q2"], "cmd": [], "help": [], "epsilon": ["q2"]},
    "q2": {"bot": [], "user": [], "cmd": ["q3"], "help": ["q3"], "epsilon": []},
    "q3": {"bot": [], "user": [], "cmd": [], "help": [], "epsilon": []}
}

DESCRIPCION_SIMBOLOS = {
    "bot": "@bot (Mención)",
    "user": "Usuario/Palabra",
    "cmd": "Comando (!cmd)",
    "help": "Comando (?help)",
    "epsilon": "Transición Lambda (Opcional)"
}

def clausura_epsilon(estados):
    clausura = set(estados)
    pila = list(estados)
    print(pila)
    while pila:
        estado = pila.pop()
        for dest in TABLA_TRANSICIONES[estado].get("epsilon", []):
            if dest not in clausura:
                clausura.add(dest)
                pila.append(dest)
    return clausura

def procesar_cadena(cadena_tokens) -> dict:
    if isinstance(cadena_tokens, str):
        cadena_tokens = cadena_tokens.split()
        
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