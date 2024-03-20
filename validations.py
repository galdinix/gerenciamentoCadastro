import re
from banco import verifiacarId
from validate_email import validate_email

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
    is_valid = validate_email(email)
    if is_valid:
        return True
    return False


def idIsValid(id):
    if verifiacarId(id):
        return True
    return False


