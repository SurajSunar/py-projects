from db import Base
from sqlalchemy import Integer, Column, String, ForeignKey, Table
from sqlalchemy.orm import relationship

class Author(Base):
    __tablename__= "Authors"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    books = relationship("Book", back_populates="author")

book_category = Table(
    "BookCategory", Base.metadata,
    Column("book_id", ForeignKey("Books.id"), primary_key=True),
    Column("category_id", ForeignKey("Categories.id"), primary_key=True)
)

class Book(Base):
    __tablename__= "Books"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    author_id = Column(Integer, ForeignKey("Authors.id"), default=None)
    author = relationship('Author', back_populates="books")
    detail = relationship('BookDetail', back_populates="book", uselist=False)

    categories = relationship(
        "Category",
        secondary=book_category,
        back_populates="books"
    )


class BookDetail(Base):
    __tablename__= "BookDetails"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    isbn = Column(String, nullable=False)
    pages = Column(Integer, nullable=False)
    publisher = Column(String, default=None)
    year = Column(Integer)
    book_id = Column(Integer, ForeignKey("Books.id"), default=None)
    book = relationship('Book', back_populates="detail")

class Category(Base):
    __tablename__= "Categories"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, nullable=False)
    books = relationship(
        "Book",
        secondary=book_category,
        back_populates="categories"
    )

