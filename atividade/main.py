from datetime import date
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
    usuarios.append(user)
    return user

#emprestimo
@app.post('/emprestimo', response_model=Emprestimo)
def emprestar_livro(emprestimo: Emprestimo):
    try:
        for livro in livros:
            for usuario in usuarios:
                if emprestimo.livro_id.id == livro.id and emprestimo.user_id.id == usuario.id and livro.disponibilidade == True:
                    livro.disponibilidade = False  
                    emprestimos.append(emprestimo)
                    return emprestimo                        
    except:
        raise HTTPException(status_code=404, detail="Algum dado inextistente")

@app.post('/devolucao', response_model=Emprestimo)
def devolucao_livro(emprestimo: Emprestimo):
    try:
        for i in emprestimos:
            for usuario in usuarios:
                for livro in livros:
                    if emprestimo.id in i.id and emprestimo.user_id.id == usuario.id and emprestimo.livro_id.id == livro.id and livro.disponibilidade == False:  
                        emprestimos.append(emprestimo)
                        return emprestimo                        
    except:
        raise HTTPException(status_code=404, detail="Algum dado inextistente")
    
@app.get('/emprestimos/{user_id}', response_model=List[Livro])
def listar_livro(user_id:str):
    livros_emprestados:List[Livro]=[]
    for emprestimo in emprestimos:
        if emprestimo.user_id.id == user_id:
            livros_emprestados.append(emprestimo.livro_id)
    return livros_emprestados
    