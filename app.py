#main.py
from fastapi import FastAPI, Query
from typing import List
import json

app = FastAPI()

@app.get("/")
def read_root():
        return {"message": "Hello, World!"}

@app.get("/api")
def find_name(names: List[str] = Query(...)):
    with open('names.json', mode='r') as file:
        data = json.load(file)
        marks = [entry['marks'] for n in names for entry in data if entry['name'] == n]
        return {"marks": marks}
