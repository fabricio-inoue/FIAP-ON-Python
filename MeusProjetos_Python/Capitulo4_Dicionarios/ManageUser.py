from MeusProjetos_Python.Capitulo4_Dicionarios.Funcoes import *

usuarios = {}
opcao = perguntar()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    if opcao == "P":
        pesquisar(usuarios, input('Qual código você deseja visualizar: '))
    if opcao == "E":
        excluir(usuarios, input('Qual código deseja excluir: '))
    if opcao == "L":
        listar(usuarios)
    opcao = perguntar()
