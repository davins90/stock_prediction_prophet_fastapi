# from fastapi import FastAPI
# from typing import Union
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None

# @app.get("/")
# def read_root():
#     return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}

# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

# from fastapi import FastAPI, Request

# app = FastAPI()

# @app.get("/sum/{a}/{b}")
# async def read_item(a: int, b: int):
#     return {"sum": a + b}


# def edit(x,y):
#     x = x*2
#     y = y*2
#     return x,y

# @app.post("/sum")
# async def read_item(request: Request):
#     data = await request.json()
#     a = data["a"]
#     b = data["b"]
#     a,b = edit(a,b)
#     return {"sum": a + b}

from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from api.model import predict, convert

app = FastAPI()

# pydantic models
class StockIn(BaseModel):
    ticker: str
    days: int

class StockOut(StockIn):
    forecast: dict
    
@app.get('/')
def get_root():
    return {'message': 'Welcome to the stock prediction API'}

@app.post("/predict", response_model=StockOut, status_code=200)
def get_prediction(payload: StockIn):
    ticker = payload.ticker
    days = payload.days

    prediction_list = predict(ticker, days)

    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")

    response_object = {
        "ticker": ticker, 
        "days": days,
        "forecast": convert(prediction_list)}
    return response_object
