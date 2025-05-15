from datetime import date
import uuid
from fastapi import FastAPI, HTTPException
from models import Livro, User, Emprestimo
from typing import List

app = FastAPI()

livros:List[Livro]=[]
usuarios:List[User]=[]
emprestimos:List[Emprestimo]=[]

#livro
@app.post('/livros', response_model=Livro)
def criar_livro(livro:Livro):
    livro.id = str(uuid.uuid4())
    livros.append(livro)
    return livro

@app.get('/livros', response_model=List[Livro])
def listar_livros():
    return livros

@app.get('/livros/{titulo}', response_model=Livro)
def listar_livro(titulo:str):
    for livro in livros:
        if livro.titulo == titulo:
            return livro
    raise HTTPException(status_code=404,detail="nao existe")
    
#user
@app.post('/users', response_model=User)
def criar_usuario(user:User):
    user.id = str(uuid.uuid4())
    usuarios.append(user)
    return user

#emprestimo
@app.post('/emprestimo', response_model=Emprestimo)
def emprestar_livro(user: str, livro: str, data_emp: date, data_dev: date):
    usuario = None
    book = None

    for x in usuarios:
        if x.id == usuario:
            usuario = x
    
    for y in livros:
        if y.id == book:
            if y.disponibilidade == True:
                book = y

    if book and usuario:
        book.disponibilidade = False
        dados = {
            "user": usuario,
            "livro": book,
            "data_emp": data_emp,
            "data_dev": data_dev
        }
        emprestimo = Emprestimo(**dados)
        emprestimos.append(emprestimo)

    raise HTTPException(status_code=404, detail="emprestimo nao realizado")
# @app.post('/devolucao', response_model=Emprestimo)
# def devolucao_livro(emprestimo: Emprestimo):
#     try:
#         for i in emprestimos:
#             for usuario in usuarios:
#                 for livro in livros:
#                     if emprestimo.id in i.id and emprestimo.user_id.id == usuario.id and emprestimo.livro_id.id == livro.id and livro.disponibilidade == False:  
#                         emprestimos.append(emprestimo)
#                         return emprestimo                        
#     except:
#         raise HTTPException(status_code=404, detail="Algum dado inextistente")
    
# @app.get('/emprestimos/{user_id}', response_model=List[Livro])
# def listar_livro(user_id:str):
#     livros_emprestados:List[Livro]=[]
#     for emprestimo in emprestimos:
#         if emprestimo.user_id.id == user_id:
#             livros_emprestados.append(emprestimo.livro_id)
#     return livros_emprestados
    