from fastapi import FastAPI
from fastapi.exceptions import HTTPException

app = FastAPI(title="my fast api",
              description="fast api handling errors"
              )
items = {"foo": "The Foo Wrestlers"}

@app.get("/items/{item_id}")
async def read_item_header(item_id:str):
    if item_id not in items:
        raise HTTPException(status_code=222,
                            detail="Items not found...",
                            headers={"X-Error":"There goes my error"})
    return {"item": items[item_id]}