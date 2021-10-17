from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

read  = FastAPI()

class Item(BaseModel):
	name: str
	price: float
	is_offer: Optional[bool] = None

@read.get("/")
def read_root():
  return {"Hello":"World"}

@read.get("/items/{item_id}")
def read_item(item_id:int, q: Optional[str]):
  if (len(q) != 0):
    return {"item_id": item_id,"q":q}
  else:
    return {"item_id":item_id}

@read.get("/items/{filePath:path}")
def read_item(filePath):
  return {"item_file_path": filePath}

@read.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
	name_str = item.name
	price_int = item.price
	if price_int > 20:
	  return {"response":200}
	else:
	  return {"response":404}
