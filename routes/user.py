from fastapi import APIRouter
from config.db import conn
from schemas.user import userEntity, usersEntity
from models.user import User
from passlib.hash import sha256_crypt
from bson import ObjectId

user = APIRouter()

@user.get('/users')
def find_all_users():
    return usersEntity(conn.local.user.find()) #find busca todos los datos en una coleccion

@user.post('/users')
def create_user(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    del new_user["id"]
    #print (new_user)
    id = conn.local.user.insert_one(new_user).inserted_id
    user=conn.local.user.find_one({"_id":id})
    return userEntity(user)
    

@user.get('/users/{id}')
def find_user(id: str):
    #print(id)
    return userEntity(conn.local.user.find_one({"_id":ObjectId(id)}))

@user.put('/users/{id}')
def update_user():
    return "hello world" 

@user.delete('/users/{id}')
def delete_user():
    return "hello world" 