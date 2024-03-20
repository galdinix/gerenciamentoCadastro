from utils import*
from banco import*

def adicionarConsulta():
    nome = receberNome()
    telefone = receberTelefone()
    email = receberEmail()
    idade = receberIdade()
    sexo = receberSexo()
    data_agendamento = receberDataAgendamento()
    especialidade = receberEspecialidade()
    adicionarNoBanco(nome, telefone, email, idade, sexo, data_agendamento, especialidade)

def deleterConsulta():
    id = receberId()
    deletarNoBanco(id)

def listar():
    id = receberId()
    opcListagem = receberOpcListagem()
    #listarNoBanco(id, opcListagem)

adicionarConsulta()

