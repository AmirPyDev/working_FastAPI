from fastapi import FastAPI, Path

app = FastAPI()


inventory = {
    1: {
        'name': 'Milk',
        'price': 3.99,
        'branch': 'regular'
    }
}

# @app.get("/get-item/{item_id}")
# def get_item(item_id: int = Path(description="the ID you'ld like to view"), le=1, gt=0):
#     return inventory[item_id]



@app.get("/get-by-name")
def get_item(name: str):
    return inventory[item_id]