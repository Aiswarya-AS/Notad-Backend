from pydantic import BaseModel,EmailStr, Field



class UserCreate(BaseModel):
    username:str
    email : EmailStr
    password : str = Field(..., min_length=4)

class ShowUser(BaseModel):
    username:str
    email:str
    is_superuser:bool
    is_active:bool

class UpdateUser(UserCreate):
    pass