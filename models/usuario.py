from typing import Optional
from pydantic import BaseModel

class Usuario(BaseModel):
    id: Optional[str]
    nombre: str
    email: str
    password: str