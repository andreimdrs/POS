from pydantic import BaseModel

class Tarefa(BaseModel):
    id: int
    desc: str
    prio: int
    conc: bool