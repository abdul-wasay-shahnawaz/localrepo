from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List

from database import engine, get_db, Base
from models import User
from schemas import UserCreate, UserResponse, UserUpdate

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Management System API",
    description="CRUD API for Users (Abdul Wasay)",
    version="1.0.0"
)

# CREATE USER
@app.post("/create-user/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        existing = db.query(User).filter(User.email == user.email).first()
        if existing:
            raise HTTPException(400, "Email already exists")

        db_user = User(**user.dict())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    except IntegrityError:
        db.rollback()
        raise HTTPException(400, "Email already exists")


# GET ALL USERS
@app.get("/users-all/", response_model=List[UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(User).all()


# GET SINGLE USER
@app.get("/user/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(404, "User not found")
    return user


# UPDATE USER
@app.put("/update-user/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(404, "User not found")

    data = user_update.dict(exclude_unset=True)

    for key, value in data.items():
        setattr(user, key, value)

    db.commit()
    db.refresh(user)
    return user


# DELETE USER
@app.delete("/delete-user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(404, "User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted successfully"}