from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Добро пожаловать в Cinema!"}


@app.get("/categories/{category_id}")
async def read_category(category_id: int):
    return {"category_id": category_id}
