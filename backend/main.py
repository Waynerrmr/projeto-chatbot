from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

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
    print("Pergunta recebida:", pergunta.pergunta)

    # Gerar resposta com o modelo Gemini
    try:
        resposta = model.generate_content(pergunta.pergunta)
        resposta_texto = resposta.text
        print("Resposta gerada:", resposta_texto)
        return {"resposta": resposta_texto}
    except Exception as e:
        print("Erro:", e)
        return {"resposta": "Ocorreu um erro ao tentar responder sua pergunta."}
