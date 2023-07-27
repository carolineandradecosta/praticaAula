import sys
import json
import re


def exibir_menu():
    print('Escolha uma opção:')
    print('1 - Cadrastrar Aluno')
    print('2 - Remover Aluno')
    print('3 - Editar Aluno')
    print('4 - Listar Aluno')
    print('5 - Sair')


def carregar_dados():
    try:
        with open('alunos.json', 'r') as arquivo:
            dados_alunos = json.load(arquivo)
    except FileNotFoundError:
        dados_alunos = []

    return dados_alunos


def salvar_dados(dados_alunos):
    with open('alunos.json', 'w') as arquivo:
        json.dump(dados_alunos, arquivo)


def validar_cpf(cpf):
    cpf = cpf.replace(".", "").replace("-", "")

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    digitos = cpf[:-2]
    soma = 0
    for i in range(9):
        soma += int(digitos[i]) * (10 - i)
    digito1 = (11 - soma % 11) % 10
    digitos += str(digito1)

    soma = 0
    for i in range(10):
        soma += int(digitos[i]) * (11 - i)
    digito2 = (11 - soma % 11) % 10
    digitos += str(digito2)

    if cpf[-2:] == digitos[-2:]:
        return True

    return False


def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(padrao, email):
        return True
    return False


def cadastrar_aluno():
    nome = input('Digite o nome do aluno: ')
    cpf = input('Digite o cpf do aluno: ')
    try:
        if validar_cpf(cpf) != True:
            raise ValueError("O CPF deve ter 11 dígitos.")

    except ValueError as m:
        print(m)
        return
    email = input('Digite o email do aluno: ')
    try:
        if validar_email(email) != True:
            raise ValueError("O e-mail é inválido.")

    except ValueError as m:
        print(m)
        return
    telefone = input('Digite o telefone do aluno: ')

    dados_alunos = carregar_dados()
    aluno = {
        'nome': nome,
        'cpf': cpf,
        'email': email,
        'telefone': telefone
    }
    dados_alunos.append(aluno)
    salvar_dados(dados_alunos)
    print('Aluno cadastrado com sucesso!')


def remover_aluno():
    nome = input('Digite o nome do aluno a ser excluído: ')
    dados_alunos = carregar_dados()
    for aluno in dados_alunos:
        if aluno['nome'] == nome:
            dados_alunos.remove(aluno)
            break
    salvar_dados(dados_alunos)
    print('Aluno excluído com sucesso!')


def editar_aluno():
    dados_alunos = carregar_dados()
    print("Digite o nome do aluno que deseja editar:")
    nome = input()
    for aluno in dados_alunos:
        if aluno["nome"] == nome:
            print("Escolha uma opção para editar:")
            print("1 - Nome")
            print("2 - CPF")
            print("3 - email")
            print("4 - Telefone")
            opcao = input()
            if opcao == "1":
                print("Digite o novo nome do aluno:")
                aluno["nome"] = input()
            elif opcao == "2":
                print("Digite o novo CPF do aluno:")
                aluno["cpf"] = input()
            elif opcao == "3":
                print("Digite o novo e-mail do aluno:")
                aluno["email"] = input()
            elif opcao == "4":
                print("Digite o novo telefone do aluno:")
                aluno["telefone"] = input()
            print("Aluno editado com sucesso!")
            salvar_dados(dados_alunos)
            break
        else:
            print("Aluno não encontrado")


def listar_alunos():
    dados_alunos = carregar_dados()
    print("Lista de alunos:")
    for aluno in dados_alunos:
        print("nome:", aluno["nome"])
        print("cpf:", aluno["cpf"])
        print("email:", aluno["email"])
        print("telefone:", aluno["telefone"])


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
