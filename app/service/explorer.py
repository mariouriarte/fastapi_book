from model.explorer import Explorer
from data import explorer as data

def get_all() -> list[Explorer]:
    return data.get_all()

def get_one(name: str) -> Explorer:
    return data.get_one(name)

def create(explorer: Explorer) -> Explorer:
    return data.create(explorer)

# def replace(id, explorer: Explorer) -> Explorer:
#     return data.replace(id, explorer)

def modify(name: str, explorer: Explorer) -> Explorer:
    return data.modify(name, explorer)

def delete(id):
    return data.delete(id)
