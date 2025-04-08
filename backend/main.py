from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import google.generativeai as genai
from backend.utils import carregar_kb, buscar_conhecimento

load_dotenv()

# No arquivo .env, adicione uma variavel GEMINI_API_KEY com a chave da API do Gemini
# Exemplo: GEMINI_API_KEY=your_api_key_here
# Ou sete diretamente nessa variável a baixo, no lugar do: os.getenv("GEMINI_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

# Classe da requisição
class Pergunta(BaseModel):
    pergunta: str

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Pode restringir a origem se quiser
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/perguntar")
async def perguntar(pergunta: Pergunta):
    kb = carregar_kb()
    conhecimento = buscar_conhecimento(pergunta.pergunta, kb)

    prompt_base = f"Pergunta: {pergunta.pergunta}\n"

    if conhecimento:
        prompt = f"O usuário perguntou algo relacionado a: \"{conhecimento}\".\nUse esse conhecimento para ajudar a formular a resposta.\n{prompt_base}"
    else:
        prompt = prompt_base

    # Gerar resposta com o modelo Gemini
    try:
        resposta = model.generate_content(prompt)
        return {"resposta": resposta.text}
    except Exception as e:
        print("Erro:", e)
        return {"resposta": "Ocorreu um erro ao tentar responder sua pergunta."}
