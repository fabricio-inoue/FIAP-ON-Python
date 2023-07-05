def perguntar():
    resposta = input("O que deseja realizar?\n"
                     "<I> - Para Inserir um usuário\n"
                     "<P> - Para Pesquisar um usuário\n"
                     "<E> - Para Excluir um usuário\n"
                     "<L> - Para Listar um usuário: ").upper()
    return resposta

def inserir(dicionario):
    dicionario[input("Digite o código do lançamento: ").upper()] = [
        input("Digite o login: ").upper(),
        input("Digite o nome: ").upper(),
        input("Digite a última data de acesso: "),
        input("Digite a última hora de acesso: "),
        input("Qual a última estação acessada: ").upper()
    ]

def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)
    if lista is not None:
        print("Nome...........:", lista[0])
        print("Último acesso..:", lista[1])
        print("Última estação.:", lista[2])

def excluir(dicionario, chave):
    if dicionario.get(chave) is not None:
        del dicionario[chave]
        print("Excluído")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print('A chave é: ', chave)
        print('O valor é: ', valor)


