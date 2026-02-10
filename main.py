from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
def main():
    return {"Hola": "Mundo"}