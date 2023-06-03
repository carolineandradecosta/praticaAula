'''A partir do ano de nascimento de uma pessoa mostrar
sua idade, se já tem idade para votar (16 anos ou
mais) e se já pode ser candidato a uma carteira de
habilitação.

* Dados de entrada: ano de nascimento
* Saída: idade, idade para votar, idade para dirigir '''

from datetime import datetime
from pytz import timezone

def calcula_idade(ano_nascimento: int):
    ano_atual = 2023
    idade_pessoa = ano_atual - ano_nascimento
    return idade_pessoa

def verifica_idade(idade: int):
    if idade >= 18:
        print('Você pode dirigir e votar')
    elif 15 < idade < 18:
        print('Você não pode dirigir e votar.')
    else:
        print('Você ainda é muito novo para essas atividades.')
    print(f'Sua idade é: {idade}')

idade = (calcula_idade(1992))
verifica_idade(idade)

date_atual = datetime.now()
print(date_atual)