from validations import*

def receberNome():
    while True:
        try:
            nome = input('Informe seu nome: ')
            if isNameValid(nome):
                return nome
            print('Erro, tente novamente')
        except Exception:
            print('Erro, tente novamente')

def receberTelefone():
    while True:
        try:
            telefone = input('Informe seu telefone: ')
            if isTelefoneValid(telefone):
                return telefone
            print('Erro, tente novamente')
        except Exception:
            print('Erro, tente novamente')

def receberEmail():
    while True:
        try:
            email = input('Informe seu email: ')
            if isEmailValid(email):
                return email
            print('Erro, tente novamente')
        except Exception:
            print('Erro, tente novamente')

def receberIdade():
    while True:
        try:
            idade = int(input('Informe sua idade: '))
            return idade
        except ValueError:
            print('Erro, tente novamente')

def receberSexo():
    while True:
        try:
            sexo = input('Informe seu sexo: ')
            return sexo
        except Exception:
            print('Erro, tente novamente')

def receberDataAgendamento():
    while True:
        try:
            data_agendamento = input('Informe a data de agendamento: ')
            return data_agendamento
        except Exception:
            print('Erro, tente novamente')

def receberEspecialidade():
    while True:
        try:
            especialidade = input('Informe a especialidade: ')
            return especialidade
        except Exception:
            print('Erro, tente novamente')

def receberId():
    while True:
        try:
            id = input('Informe o id: ')
            if idIsValid(id):
                return id
            print('Erro, tente novamente')
        except Exception:
            print('Erro, tente novamente')

def receberOpcListagem():
    while True:
        try:
            opc = input('Deseja listar por nome(N), idade(I), sexo(S), data_agendamento(DA), especialidade(E), listagem completa(LC): ').upper()
            if opc == 'N':
                return 'nome'
            if opc == 'S':
                return 'sexo'
            if opc == 'DA':
                return 'data_agendamento'
            if opc == 'E':
                return 'especialidade'
            if opc == 'I':
                return 'idade'
            if opc == 'LC':
                return '*'
            print('Erro, tente novamente')
        except Exception:
            print('Erro, tente novamente')