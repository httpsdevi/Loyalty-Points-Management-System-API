from fastapi import FastAPI, HTTPException
from schemas import UserCreate, Transaction, Redemption
import crud

app = FastAPI()

@app.post("/register")
def register_user(user: UserCreate):
    try:
        crud.create_user(user.name, user.email)
        return {"msg": "User registered successfully."}
    except:
        raise HTTPException(status_code=400, detail="Email already registered.")

@app.post("/earn")
def earn_points(transaction: Transaction):
    if crud.get_user(transaction.email):
        crud.add_points(transaction.email, transaction.amount)
        return {"msg": "Points added."}
    raise HTTPException(status_code=404, detail="User not found.")

@app.post("/redeem")
def redeem_points(data: Redemption):
    success = crud.redeem_points(data.email, data.points)
    if success:
        return {"msg": "Points redeemed."}
    raise HTTPException(status_code=400, detail="Insufficient points.")
