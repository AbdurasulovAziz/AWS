from fastapi import HTTPException
from sqlalchemy import select, update
from sqlalchemy.orm import Session

from transitionzero.goodreads.models.database import Book


class ServiceBooks:

    def search(self, db: Session, user_id: int):
        obj = db.execute(select(Book).where(Book.id == user_id)).scalar()
        if not obj:
            raise HTTPException(status_code=404, detail="Book not found")

        return obj

    def get(self, db: Session):
        return db.execute(select(Book)).scalars().all()

    def post(self, db: Session, data: dict):
        new_book = Book(**data)
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        return new_book

    def patch(self, db: Session, book_id: int, data: dict):
        db.execute(update(Book).where(Book.id == book_id).values(**data))
        db.commit()


    def delete(self, db: Session, book_id: int):
        obj = self.search(db, book_id)
        db.delete(obj)
        db.commit()

service_books = ServiceBooks()