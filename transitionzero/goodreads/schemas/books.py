from pydantic import BaseModel


class BookSchemaBase(BaseModel):
    title: str
    genre: str
    year: int


class BookSchema(BookSchemaBase):
    id: int