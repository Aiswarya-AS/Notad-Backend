from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List
from schemas.user import UserCreate, ShowUser, UpdateUser
from db.session import get_db
from db.repository.user import create_new_user, retreive_user, retreive_users, update_user, delete_user

router = APIRouter()


@router.post("/")
def create_user(user : UserCreate,db: Session = Depends(get_db)):
    user = create_new_user(user=user,db=db)
    return user 

@router.get("/user/{id}", response_model=ShowUser)
def read_user(id:int, db: Session = Depends(get_db)):
    user  = retreive_user(id=id, db=db)
    return user

@router.get("/users", response_model=List[ShowUser])
def read_users(db: Session = Depends(get_db)):
    users = retreive_users(db=db)
    return users

@router.put("/user/{id}", response_model=UpdateUser)
def update_a_user(id:int, user:UpdateUser, db: Session = Depends(get_db)):
    user  = update_user(id, user, db)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/user/{id}")
def delete_a_user(id:int, db: Session = Depends(get_db)):
    message  = delete_user(id=id, db=db)
    if message.get("error"):
        raise HTTPException(detail=message.get("error"), status_code= status.HTTP_400_BAD_REQUEST)
    return message