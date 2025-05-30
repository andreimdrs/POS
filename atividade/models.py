from typing import Optional
from pydantic import BaseModel
from datetime import date

class Livro(BaseModel):
    id: str
    titulo: str
    autor: str
    ano: int
    disponibilidade: bool

class User(BaseModel):
    id: str
    nome: str
    livros: list[Livro]

class Emprestimo(BaseModel):
    user: User
    livro: Livro
    data_emp: date
    data_dev: Optional[date] = None
