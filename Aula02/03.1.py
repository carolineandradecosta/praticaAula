'''Um programa que permita saber qual o peso ideal de
uma pessoa.
● Para homens: (72,7 * h) - 58
● Para mulheres: (62,1 * h) - 44,7

Dados de entrada: altura e sexo de uma pessoa.'''

print('--- Iniciando o cálculo do peso ideal---')

genero = input('Digite seu gênero (M ou F): ').upper()
h = float(input('Digite sua altura: '))

if genero == 'F':
    peso_ideal = (62.1 * h) - 44.7
elif genero == 'M':
    peso_ideal = (72.7 * h) - 58
else:
    print('Gênero incorreto')

print(f'Você que é do gênero {genero} tem peso ideal {peso_ideal:0.2f}')



