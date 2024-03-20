import re
from banco import verifiacarId
from validate_email import validate_email
import phonenumbers

def isNameValid(nome):
    if len(nome) > 3:
        return True
    return False

def isTelefoneValid(telefone):
    try:
        telefone_formatado = phonenumbers.parse(telefone, None)
        # Verificar se é um número de telefone válido
        is_valid = phonenumbers.is_valid_number(telefone_formatado)
        return is_valid
    except phonenumbers.phonenumberutil.NumberParseException:
        return False

def  isEmailValid(email):
    is_valid = validate_email(email)
    if is_valid:
        return True
    return False


def idIsValid(id):
    if verifiacarId(id):
        return True
    return False


