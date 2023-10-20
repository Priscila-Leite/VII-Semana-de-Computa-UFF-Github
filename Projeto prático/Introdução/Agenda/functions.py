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

def buscar(nome=None, telefone=None):
    if nome == telefone == None:
        return False
    if nome != None:
        for contato in contatos:
            if contato['nome'] == nome:
                return contato
        return None
    if telefone != None:
        for contato in contatos:
            if contato['telefone'] == telefone:
                return contato
        return None
    
    

# Deletar contatos


