from fastapi import FastAPI, APIRouter
from transitionzero.goodreads.views.books import router as books_router

router = APIRouter()

@router.get("/")
def health():
    return "healthy!"

app = FastAPI(title="tz_goodreads")
app.include_router(router)
app.include_router(books_router)