from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI, Query, Body

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

app = FastAPI()

@app.put("/items/{item_id}")
async def update_item(item_id:int,
                      item: Item = Body(...,embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
