# ChatBot Acadêmico

## 👥 Integrantes
- WAYNER RORAN MORAES ROLIM / 202100023048
- JOSÉ ANTONIO DE GOES NETO / 202100022828
- ALMIR VINÍCIUS BISPO DO NASCIMENTO / 202100011181

## 📌 Visão Geral
Um chatbot simples que responde perguntas acadêmicas consultando internet em geral e usando um modelo da Gemini-1.5-flash.

## 📂 Estrutura do Projeto
```
projeto-chatbot/
│── backend/
│   ├── kb.json     # Knowledge Base
│   ├── main.py     # API de comunicação com Gemini utilizando FastAPI
│   ├── utils.py    # Funções auxiliares (consulta à KB)
│── frontend/           # Diretório onde está a página web
│   ├── index.html      # Página web
│── requirements.txt    # Lista de dependências do projeto
│── .env                # Chave da API do Gemini
│── README.md           # Documentação do projeto
```

## Requisitos
- Python 3.8+ (foi utilizado o [python 3.12.3](https://www.python.org/downloads/release/python-3123/))
- Uma [chave de API da Gemini](https://ai.google.dev/gemini-api/docs/api-key)

## 🛠️ Dependências
As dependências do projeto estão listadas no arquivo `requirements.txt`.

### 📥 Instalando as dependências
Execute o comando abaixo para instalar todas as bibliotecas necessárias:
```sh
pip install -r requirements.txt
```

## 🚀 Execução
```bash
uvicorn backend.main:app --reload
```

Abra o arquivo `frontend/index.html` no navegador e faça perguntas!

## 📄 Relatório/Artigo Técnico-Científico
- [Versão em português](https://link_da_versao_em_portugues.com)
- [Versão em inglês](https://link_da_versao_em_ingles.com)