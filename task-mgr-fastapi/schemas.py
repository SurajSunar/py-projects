from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str

class Author(AuthorBase):
    id: int
    
    class Config:
        orm_mode = False

class AuthorCreate(AuthorBase):
    pass

class BookBase(BaseModel):
    title: str
     description: str
    year: int
    author: Author
    
class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class config:
        from_attribute = True

