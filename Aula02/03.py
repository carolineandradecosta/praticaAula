'''Um programa que permita saber qual o peso ideal de
uma pessoa.
● Para homens: (72,7 * h) - 58
● Para mulheres: (62,1 * h) - 44,7

Dados de entrada: altura e sexo de uma pessoa.'''


def calcula_peso_ideal(altura: float, sexo: str):
    if sexo == 'homem':
        return (72.7 * altura) - 58
    elif sexo == 'mulher':
        return (62.1 * altura) - 44.7

print(calcula_peso_ideal(1.61, 'homem'))
