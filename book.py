from fastapi import APIRouter
api_book = APIRouter()
@api_book.get("/")
async def list_books():
    return [{"id": 1, "title": "Example Book"}]

