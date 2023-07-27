import sys

alunos = []


def exibe_menu():
    print("Escolha uma opção")
    print("1 - Cadastra Aluno")
    print("2 - Deleta Aluno")
    print("3 - Edita Aluno")
    print("4 - Lista Alunos")
    print("5 - Sair")


def cadastrar_aluno():
    print("Digite o nome do aluno:")
    nome = input()
    print("Digite o cpf do aluno:")
    cpf = input()
    print("Digite o email do aluno:")
    email = input()
    print("Digite o telefone do aluno:")
    telefone = input()
    alunos.append({"nome": nome, "cpf": cpf, "email": email, "telefone": telefone})


def deletar_aluno():
    print("Digite o nome do aluno que deseja remover: ")
    nome = input()
    for aluno in alunos:
        if aluno["nome"] == nome:
            alunos.remove(aluno)
            print("Aluno removido com sucesso!")
            break
        else:
            print("Aluno não encontrado")


def editar_aluno():
    print("Digite o nome do aluno que deseja editar:")
    nome = input()
    for aluno in alunos:
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
            break
        else:
            print("Aluno não encontrado")


def listar_aluno():
    print("Lista de alunos:")
    for aluno in alunos:
        print("nome:", aluno["nome"])
        print("cpf:", aluno["cpf"])
        print("email:", aluno["email"])
        print("telefone:", aluno["telefone"])


def sair():
    sys.exit()


while True:
    exibe_menu()
    opcao = input()

    if opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        deletar_aluno()
    elif opcao == "3":
        editar_aluno()
    elif opcao == "4":
        listar_aluno()
    elif opcao == "5":
        sair()
    else:
        print("Opição inválida!")
