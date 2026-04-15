from fastapi import FastAPI
from pydantic import BaseModel

# Criando a aplicação FastAPI
app = FastAPI(
    title="API de Análise de Sentimentos",
    description="API REST desenvolvida para a Fase 1 da disciplina, contendo um método GET e um método POST.",
    version="1.0.0"
)

# Método POST
class TextoEntrada(BaseModel):
    texto: str

# Método GET
@app.get("/")
def home():
    return {
        "mensagem": "API de análise de sentimentos funcionando com sucesso"
    }

# Método POST para receber um texto e retornar
@app.post("/sentimento")
def analisar_sentimento(dados: TextoEntrada):
    texto = dados.texto.lower()

    # Classificação do sentimento
    if "feliz" in texto or "ótimo" in texto or "bom" in texto or "excelente" in texto:
        sentimento = "positivo"
    elif "triste" in texto or "ruim" in texto or "péssimo" in texto or "horrível" in texto:
        sentimento = "negativo"
    else:
        sentimento = "neutro"

    return {
        "texto_recebido": dados.texto,
        "sentimento": sentimento,
        "observacao": "Esta API está preparada para futura integração com um modelo de IA para análise de sentimentos."
    }
