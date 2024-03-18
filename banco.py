import sqlite3


def adicionarNoBanco(nome, telefone, email, idade, sexo, data_agendamento, especialidade):
    conexao, cursor = criarConexaoAndCurosr()

    #criando tabela pessoas
    cursor.execute('CREATE TABLE IF NOT EXISTS visitantes (id INTEGER PRIMARY KEY, nome TEXT, telefone TEXT, email TEXT, IDADE INTEGER, sexo TEXT, data_agendamento TEXT, especialidade TEXT)')
    cursor.execute('INSERT INTO  visitantes(nome, telefone, email, idade, sexo, data_agendamento, especialidade) VALUES (?,?, ?,?,?,?,?)', (nome, telefone, email, idade, sexo, data_agendamento, especialidade))
    
    conexao.commit()

    cursor.execute('SELECT * FROM visitantes')
    pessoas = cursor.fetchall()

    for pessoa in pessoas:
        print(pessoa)

    conexao.close()

def criarConexaoAndCurosr():
    conexao = sqlite3.connect('visitantes.db')
    cursor = conexao.cursor()
    return conexao, cursor


def verifiacarId(id):
    conexao, cursor = criarConexaoAndCurosr()
    cursor.execute("SELECT COUNT(*) FROM visitantes WHERE id = ?", (id,))
    resultado = cursor.fetchone()[0]
    conexao.close()
    return resultado > 0

def deletarNoBanco(id):
    conexao, cursor = criarConexaoAndCurosr()
    cursor.execute("DELETE FROM visitantes WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()