from fastapi import APIRouter
from config.db import conn
from schemas.user import userEntity, usersEntity
from models.user import User

user = APIRouter()

@user.get('/users')
def find_all_users():
    return usersEntity(conn.local.user.find()) #find busca todos los datos en una coleccion

@user.post('/users')
def create_user(user: User):
    new_user = dict(user)
    del new_user["id"]
    #print (new_user)
    id = conn.local.user.insert_one(new_user).inserted_id
    user=conn.local.user.find_one({"_id":id})
    return userEntity(user)
    

@user.get('/users/{id}')
def find_user():
    return "hello world" 

@user.put('/users/{id}')
def update_user():
    return "hello world" 

@user.delete('/users/{id}')
def delete_user():
    return "hello world" 