from fastapi import FastAPI 
from pydantic import BaseModel

class MessageHistorique(BaseModel) :
    role: str
    dioula: str
    francais: str

class ChatRequest(BaseModel) :
    message: str
    historique: list[MessageHistorique]

app = FastAPI()
@app.post("/chat")
def requete_demander(requete: ChatRequest) -> dict :
    with verrou_gpu :
        reponse, nouvel_historique = repondre(requete.message, requete.historique)
    return {
        "reponse" : reponse,
        "historique" : nouvel_historique
    }
