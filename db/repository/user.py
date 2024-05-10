from sqlalchemy.orm import Session

from schemas.user import UserCreate, UpdateUser
from db.models.user import User
from core.hashing import Hasher


def create_new_user(user:UserCreate,db:Session):
    user = User(
        username=user.username,
        email = user.email,
        password=Hasher.get_password_hash(user.password),
        is_active=True,
        is_superuser=False
        )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def retreive_user(id:int, db:Session):
    user = db.query(User).filter(User.id==id).first()
    return user

def retreive_users( db:Session):
    users = db.query(User).filter(User.is_active==True).all()
    return users


def update_user(id:int, user:UpdateUser, db:Session):
    user_in_db = db.query(User).filter(User.id==id).first()
    if not user_in_db:
        return None
    user_in_db.username=user.username
    user_in_db.email=user.email
    db.add(user_in_db)
    db.commit()
    return user_in_db

def delete_user(id:int, db:Session):
    user = db.query(User).filter(User.id==id)
    if not user:
        return {"error":f"Could not find user with id {id}"}
    user.delete()
    db.commit()
    return {"msg":f"deleted user with id {id}"}