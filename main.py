from fastapi import FastAPI
from models import Item

app = FastAPI()


# welcome message
@app.get('/')
def welcome():
    return {'mensaje': 'Welcome to the items main app'}



@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict