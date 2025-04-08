import json

def carregar_kb():
    with open("backend/kb.json", "r", encoding="utf-8") as f:
        return json.load(f)

def buscar_conhecimento(pergunta, kb):
    for chave, valor in kb.items():
        if chave.lower() in pergunta.lower():
            return valor
    return None
