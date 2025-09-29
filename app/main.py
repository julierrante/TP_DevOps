

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

#app = FastAPI(title="AfiliadoCheck API", version="1.0.0")


@app.get("/") # endpoint que redirige a /docs
def root():
    return RedirectResponse(url="/docs")

#@app.get("/health")
#def health_check():
#    return{"status": "ok"}

@app.get("/check-member/{name}")
def check_member(name: str):
    return {"registered": name.lower() in members}


# Base de datos en memoria (solo para el TP)
members = {
    "jazmin": True,
    "maria": True,
    "juan": False
}



