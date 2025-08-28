from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def home():
    return {"message": "API Calculadora"}

@app.get("/soma/")
def soma(x: int, y: int):
    return {"soma": x+y}

@app.get("/raizCubica/")
def raizC(num: int):
    return {f'raiz cubica = {num ** (1/3)}'}

@app.get("/raiz-quadrada/")
def raiz_quadrada(radicando: int):
    return {f"raiz quadrada de {radicando}": radicando ** (1/2)}

@app.get("/divisao/")
def divisao(x: int, y:int):
    return {"divisao": x / y}

