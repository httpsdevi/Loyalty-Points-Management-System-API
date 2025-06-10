from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class Transaction(BaseModel):
    email: EmailStr
    amount: float

class Redemption(BaseModel):
    email: EmailStr
    points: int
