from pydantic import BaseModel

class user(BaseModel):
    username: str
    password: str
    email: str

# class Ticket(BaseModel):
#     ticket_id: int
#     date: str
#     origin: str
#     destination: str

