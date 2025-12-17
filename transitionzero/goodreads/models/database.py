import os

from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# Create on DB connection
DB_PW = os.environ.get("POSTGRES_PASSWORD")
DB_HOST = os.environ.get("PG_DB_HOST")
DB_PORT = os.environ.get("PG_DB_PORT")
DB_NAME = os.environ.get("PG_DB_NAME")
print(DB_HOST)
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://postgres:password@localhost:5432/tz_goodreads"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """ Utility to create a local db session. """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)

    books = relationship("Book", back_populates="author", passive_deletes=True)


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    genre = Column(String)
    year = Column(Integer)
    times_read = Column(Integer)

    author = relationship("Author", back_populates="books")
    author_name = Column(String, ForeignKey("authors.name", ondelete="CASCADE"))