from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

data = []

class Book(BaseModel):
    title:str
    author:str
    publisher:str
    price: float

@app.post("/book/")
async def create(book:Book):
    data.append(book.dict())
    return data

@app.get("/{id}")
async def read_book(id: int):
    return data[id]

@app.get("/")
async def read_book():
    return data

@app.put("/item/{id}")
async def update(id: int, book: Book):
    data[id] = book
    return book

@app.delete("/book/{id}")
async def delete_book(id: int):
    data.pop(id)
    return data