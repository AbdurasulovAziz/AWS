from fastapi import FastAPI, APIRouter

router = APIRouter()

@router.get("/")
def health():
    return "healthy!"

app = FastAPI(title="tz_goodreads")
app.include_router(router)