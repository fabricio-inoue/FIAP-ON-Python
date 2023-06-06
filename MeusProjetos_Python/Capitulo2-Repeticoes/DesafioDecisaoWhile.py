resposta='SIM' 

while resposta == 'SIM':
    nivel_acesso=input('Digite o nível de acesso para ADM, USR ou GUEST: ').upper()
    if nivel_acesso == 'ADM' or nivel_acesso == 'USR':
        genero=input('Digite o gênero para MASCULINO ou FEMININO: ').upper()
        if genero == 'FEMININO':
            if nivel_acesso == 'ADM':
                print('Olá administradora ')
            elif nivel_acesso == 'USR':
                print('Olá usuária ')
        else:
            if nivel_acesso == 'ADM':
                print('Olá administrador ')
            elif nivel_acesso == 'USR':
                print('Olá usuário ')

    elif nivel_acesso == 'GUEST':
        print('Olá visitante ')

    else:
        print('Olá desconhecido(a)')
    resposta=input("Digite SIM para continuar: ").upper()