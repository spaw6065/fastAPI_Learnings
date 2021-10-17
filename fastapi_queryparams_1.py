from fastapi import FastAPI, Query 
from typing import Optional

app = FastAPI()

@app.get("/items/")
async def read_items(
    q:Optional[str] = Query(None, 
                            min_length = 2, 
                            max_length = 20,
                            alias = "item-query",
                            description = "Enter the item elements",
                            deprecated = True)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q":q})
    return results