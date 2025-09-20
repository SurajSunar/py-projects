from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLAlchemy_URL = 'postgresql://surbhu:surbhu@localhost:5432/bookstore'

engine = create_engine(SQLAlchemy_URL)

SessionLocal = sessionmaker(autocommit= False, autoflush= False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_table():
    Base.metadata.create_all(bind=engine)