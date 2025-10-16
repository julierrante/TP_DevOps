from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
def root():
    return RedirectResponse(url="/docs")

@app.get("/health")
def health_check():
   return{"status": "ok"}

@app.get("/check-member/{name}")
def check_member(name: str):
    return {"registered": name.lower() in members}

members = [
    "jazmin",
    "maria",
    "juana"
]
