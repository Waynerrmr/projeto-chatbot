from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import openai
import wikipedia
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# Permitir o frontend acessar
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Pergunta(BaseModel):
    pergunta: str

@app.post("/perguntar")
def responder(pergunta: Pergunta):
    try:
        contexto = wikipedia.summary(pergunta.pergunta, sentences=2)
    except:
        contexto = "Não foi possível encontrar nada na Wikipedia."

    prompt = f"Com base no seguinte contexto, responda de forma clara e objetiva:\n\n{contexto}\n\nPergunta: {pergunta.pergunta}"

    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente acadêmico útil."},
            {"role": "user", "content": prompt}
        ]
    )

    return {"resposta": resposta.choices[0].message.content}