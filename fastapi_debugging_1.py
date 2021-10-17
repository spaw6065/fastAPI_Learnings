from fastapi import FastAPI
from starlette.routing import Host
import uvicorn

app = FastAPI(title="testApp", description="Testing the debug functionality")

@app.get("/items/{item_id}")
async def read_items(item_id:str):
    status_code = 200
    return status_code

if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8100)