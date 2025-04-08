# ChatBot Acadêmico

## 👥 Integrantes
- WAYNER RORAN MORAES ROLIM / 202100023048
- JOSÉ ANTONIO DE GOES NETO / 202100022828
- ALMIR VINÍCIUS BISPO DO NASCIMENTO / 202100011181

## 📌 Visão Geral
Um chatbot simples que responde perguntas acadêmicas, voltado a [UFS](https://www.ufs.br/) (Universidade Federal de Sergipe), consultando a internet em geral, pelo modelo da Gemini-1.5-flash e uma base de conhecimentos locais (arquivo `backend/kb.json`).

## 📂 Estrutura do Projeto
```
projeto-chatbot/
│── backend/
│   ├── kb.json     # Knowledge Base
│   ├── main.py     # API de comunicação com Gemini utilizando FastAPI
│   ├── utils.py    # Funções auxiliares (consulta à KB)
│── frontend/
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

Execute os comandos e faça perguntas!

### 1 - Frontend
```bash
start ./frontend/index.html
```
### 2 - Backend
```bash
uvicorn backend.main:app --reload
```

## 📄 Relatório/Artigo Técnico-Científico
- [Versão em português](https://link_da_versao_em_portugues.com)
- [Versão em inglês](https://link_da_versao_em_ingles.com)