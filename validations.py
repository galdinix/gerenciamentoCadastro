import re
from banco import verifiacarId

def isNameValid(nome):
    if len(nome) > 3:
        return True
    return False

def isTelefoneValid(telefone):
    telefone = re.sub(r'\D', '', telefone)
    if len(telefone) < 9:
        return False
    return True

def  isEmailValid(email):
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(regex, email):
        return True
    return False

def idIsValid(id):
    if verifiacarId(id):
        return True
    return False


