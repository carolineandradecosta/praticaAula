with open('teste\\arquivo02.txt', 'r', encoding ='utf-8') as file_object:
    conteudo = file_object.read()
    print(f'Tipo: {type(conteudo)} \n{conteudo}')


# Outra alternativa: guardar em variáveis
diretorio = 'teste\\'
arquivo = 'arquivo02.txt'
filepath = diretorio + arquivo

with open(filepath, 'r', encoding='utf-8') as file_object:
    conteudo = file_object.read()
    print(f'Tipo: {type(conteudo)} \n{conteudo}')

