from typing import Optional
from uuid import UUID
from fastapi import FastAPI, Body, Header, status, Form
from datetime import datetime, time, timedelta 
app = FastAPI()

@app.put("/items/{item_id}",status_code = status.HTTP_201_CREATED)
async def read_items(
    item_id: UUID,
    start_datetime: Optional[datetime] = Body(datetime.now()),
    end_datetime: Optional[datetime] = Body(datetime.now()), 
    repeat_at: Optional[time] = Body(None),
    process_after: Optional[timedelta] = Body(None),
    input_type: Optional[str] = Header(None),
    username: str = Form(...),
    password: str = Form(...)
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process

    return  {"item_id": item_id,
            "start_datetime": start_datetime,
            "end_datetime": end_datetime,
            "repeat_at": repeat_at,
            "process_after": process_after,
            "start_process": start_process,
            "duration": duration,
            "username": username,
            "password": password
            }

