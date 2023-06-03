# 1 - Adicionar pessoas
# 2 - Pesquisar uma pessoa
# 3 - Listar

lista = ['Carol', 'Mel', 'Gael', 'Celiane']

while True:

    print('1 - Adicionar \n2 - Pesquisar\n3 - Listar\n4 - Remover')
    opcao = int(input('Digite a opcção desejada: '))

    if opcao == 1:
        nome_pessoa = input('Digite o nome da pessoa: ')
        lista.append(nome_pessoa)
    elif opcao == 2:
        nome_pesquisa = input('Digite o nome a pesquisa: ')
        if nome_pesquisa in lista:
            print(f'O nome {nome_pesquisa} está na lista')
    elif opcao == 3:
        for nome in lista:
            print(f' ->{nome}')
    elif opcao == 4:
        nome_remover = input('Informe o nome que deseja remover: ')
        if nome_remover in lista:
            lista.remove(nome_remover)
        else:
            print('Nome não encontrados!')
    elif opcao == 5:
        nome_alterar = input('Digite o nome a ser alterado: ')
        if nome_alterar in lista:
            alteracao = input('Qual será o novo nome? ')
            lista[lista.index(nome_alterar)] = alteracao
    else:
        print('O nome não foi encontrado! ')