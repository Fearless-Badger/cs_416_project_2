from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

items = []
items.append("apple")

@app.get("/")
def root():
    return {"Hello" : "World"} # Json

@app.get("/create")
def create_item(item: str):
    items.append(item)
    return json.dumps(items)

@app.get("/retrieve/{item_id}")
def retrieve_item(item_id: int):
    if -1 < item_id < len(items):
        return json.dumps(items[item_id])
    raise HTTPException(status_code=404, detail = "Item not found")