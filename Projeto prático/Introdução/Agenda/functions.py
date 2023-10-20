contatos = []

# Adicionar contatos
def add():
    nome = input('Nome: ')
    telefone = int(input('Telefone: '))
    contato = {
        'nome': nome,
        'telefone': telefone
    }
    contatos.append(contato)
    return True
