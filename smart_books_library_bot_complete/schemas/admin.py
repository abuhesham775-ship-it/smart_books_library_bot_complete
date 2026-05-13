from pydantic import BaseModel


class AdminStats(BaseModel):
    users: int = 0
    books: int = 0
    reviews: int = 0
    points: int = 0
    challenges: int = 0
