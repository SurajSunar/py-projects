from fastapi import FastAPI, Depends, HTTPException
import services, models, schemas
from db import engine, get_db
from sqlalchemy.orm import Session
from typing import List

app = FastAPI()

##### Books
@app.get('/books', response_model=list[schemas.Book])
async def get_books(db: Session = Depends(get_db)):
    return services.get_books(db)

@app.post('/books', response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    return services.create_book(db, book)

@app.get('/books/{book_id}', response_model= schemas.Book)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    return services.get_book_by_id(db, book_id)

@app.put('/books/{book_id}', response_model= schemas.Book)
def update_book_by_id(book: schemas.BookCreate, book_id: int, db: Session = Depends(get_db)):
    update_item = services.update_book(db, book, book_id)
    if update_item:
        return update_item
    raise HTTPException(status_code=404, detail="Item not found")


@app.delete('/books/{book_id}', response_model= schemas.Book)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    delete_item = services.delete_book(db, book_id)
    if delete_item:
        return delete_item
    raise HTTPException(status_code=404, detail="Item not found")


##### authors
@app.get('/authors', response_model=list[schemas.Author])
async def get_authors(db: Session = Depends(get_db)):
    return services.get_authors(db)

@app.post('/authors', response_model=schemas.Author)
async def get_authors(author: schemas.AuthorCreate, db: Session = Depends(get_db)):
    return services.create_author(db, author)

##### category
@app.get('/categories', response_model=list[schemas.Category])
async def get_categories(db: Session = Depends(get_db)):
    return services.get_categories(db)

@app.post('/categories', response_model=schemas.Category)
async def create_category(author: schemas.CategoryBase, db: Session = Depends(get_db)):
    return services.create_category(db, author)