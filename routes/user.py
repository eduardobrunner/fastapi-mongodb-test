from fastapi import APIRouter

user = APIRouter()

@user.get('/users')
def helloworld():
    return "hello world"