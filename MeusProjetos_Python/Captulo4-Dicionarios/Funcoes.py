def perguntar():
    return input('O que deseja realizar?\n' +
                 '<I> Para inserir usuário\n' +
                 '<P> Para pesquisar usuário\n' +
                 '<E> Para excluir usuário\n' +
                 '<L> Para listar usuário\n').upper()

def inserir(Dicionario):
    usuarios[input("Digite a chave").upper()] = [input("Digite o nome").upper(), input("Digite a data"),
                                                 input("Digite a estação").upper()]