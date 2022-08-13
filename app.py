from fastapi import FastAPI
from routes.user import user

app = FastAPI() #me devuelve un objeto app

app.include_router(user)
