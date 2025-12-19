
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from transitionzero.goodreads.services.books import service_books
from transitionzero.goodreads.models.database import get_db
from transitionzero.goodreads.schemas.books import BookSchema, BookSchemaBase

router = APIRouter()

@router.get("/books", response_model=list[BookSchema])
def get_books(
        session: Session = Depends(get_db)):
    return service_books.get(session)

@router.get("/search/{book_id}", response_model=BookSchema)
def get_book_by_id(
        book_id: int,
        session: Session = Depends(get_db)
):
    return service_books.search(session, book_id)

@router.post("/books", response_model=BookSchema)
def create_book(
        book: BookSchemaBase,
        session: Session = Depends(get_db)
):
    return service_books.post(session, book.model_dump())

@router.patch("/books/{book_id}")
def patch_book(
        book_id: int,
        book: BookSchemaBase,
        session: Session = Depends(get_db)
):
    return service_books.patch(session, book_id, book.model_dump(exclude_unset=True))

@router.delete("/books/{book_id}")
def delete_book(
        book_id: int,
        session: Session = Depends(get_db)
):
    return service_books.delete(session, book_id)