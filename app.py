from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata

app = FastAPI(
    title="MI APLICAION CON FastAPI y Mongodb",
    description="esta es una pequeña api de prueba",
    version="0.0.1",
    openapi_tags=tags_metadata
) #me devuelve un objeto app

app.include_router(user)
