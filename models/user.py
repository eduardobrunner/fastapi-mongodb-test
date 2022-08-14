import email
from unicodedata import name
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: Optional[str] #el id no es necesario que me lo pasen. Como es opcional importo Optional desde typing
    name: str
    email: str
    password: str