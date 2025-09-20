from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    name: str

class Category(CategoryBase):
    id: int
    class BookNested(BaseModel):
        id: int
        title: str
        description: str
    books: Optional[list[BookNested]] = []

    class config:
        from_attribute = True

class BookBase(BaseModel):
    title: str
    description: str
    
class BookCreate(BookBase):
    author_id: Optional[int] = None
    categories: Optional[list[int]] = None


class Book(BookBase):
    id: int
    class AuthorNested(BaseModel):
        id: int
        name: str

    author: Optional[AuthorNested] = None
    categories: Optional[list[Category]] = []
    class config:
        from_attribute = True


class AuthorBase(BaseModel):
    name: str

class Author(AuthorBase):
    id: int
    books: Optional[list[Book]] = None
    
    class Config:
        from_attributes = True

class AuthorCreate(AuthorBase):
    pass

