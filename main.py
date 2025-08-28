from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API Calculadora"}

@app.get("/soma/")
def soma(x: int, y: int):
    return {"soma": x+y}
