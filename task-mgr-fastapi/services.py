from models import Book, Author
from sqlalchemy.orm import Session
from schemas import BookCreate, AuthorCreate
from sqlalchemy import Update

def create_book(db: Session, data: BookCreate):
    book_instance = Book(**data.model_dump())
    db.add(book_instance)
    db.commit()
    db.refresh(book_instance)
    return book_instance

def get_books(db: Session):
    return db.query(Book).all()

def get_book_by_id(db: Session, id: int):
    return db.query(Book).filter(Book.id == id).first()

def update_book(db: Session, data: Book, id: int):
    db_item = db.query(Book).filter(Book.id == id).first()
    if db_item is None:
        return db_item
    
    item_data = data.model_dump(exclude_unset=True) # Exclude_unset for partial updates
    for key, value in item_data.items():
        setattr(db_item, key, value)

    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete_book(db: Session, id: int):
    db_item = db.query(Book).filter(Book.id == id).first()

    if db_item is None:
        return db_item

    db.delete(db_item)
    db.commit()
    return db_item


def get_authors(db: Session):
    return db.query(Author).all()


def create_author(db: Session, data: AuthorCreate):
    author_instance = Author(**data.model_dump())
    db.add(author_instance)
    db.commit()
    db.refresh(author_instance)
    return author_instance
