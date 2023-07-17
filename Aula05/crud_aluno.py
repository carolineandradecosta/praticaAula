import sys


def exibir_menu():
    print('Escolha uma opção:')
    print('1 - Cadrastrar Aluno')
    print('2 - Remover Aluno')
    print('3 - Editar Aluno')
    print('4 - Listar Aluno')
    print('5 - Sair')


def cadastrar_aluno():
    print("Salvar esse aluno em um arquivo em formato JSON\n")
    # Fazer uma exception para verificar se o CPF tem 11 digitos
    # Validar o email (ChatGPT: faça uma função em python que valida se o email é real ou não)
    # Pesquisar expressões regulares (regex) e banco de dados minimalista
    # Fazer uma lista para salvar esses alunos


def remover_aluno():
    print('Essa função remove o aluno da lista, ou arquivo, ou banco de dados')


def editar_aluno():
    print('Essa função vai remover um aluno da lista e adicionar o nome atualizado')


def listar_alunos():
    print('Essa função vai listar os alunos cadastrados')


def fechar_programa():
    sys.exit()


while True:
    exibir_menu()
    escolha = input()

    if escolha == '1':
        cadastrar_aluno()
    elif escolha == '2':
        remover_aluno()
    elif escolha == '3':
        editar_aluno()
    elif escolha == '4':
        listar_alunos()
    else:
        # Fazer o tratamento de exessão para não deixar o número maior que 5 e menor que 1
        fechar_programa()
