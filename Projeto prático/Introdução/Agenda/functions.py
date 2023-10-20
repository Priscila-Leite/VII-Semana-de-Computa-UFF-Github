contatos = []

# Adicionar contatos
def adicionar():
    nome = input('Nome: ')
    telefone = int(input('Telefone: '))
    contato = {
        'nome': nome,
        'telefone': telefone
    }
    contatos.append(contato)
    return True

# Listar contatos

def listar():
    if len(contatos) > 0:
        for contato in contatos:
            print(contato['nome'], '....', contato['telefone'])
        return True
    return False

# Buscar contatos



# Deletar contatos


