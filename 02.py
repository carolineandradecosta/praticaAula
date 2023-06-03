
print('--- Iniciando programa de idade ---')

idade = int(input('Digite a sua idade: '))


# Estrutura condicional IF

# if idade >= 18 and tipo_ingresso == 'VIP':
#     print('Você pode entrar na festa!')
#     print('Pode seguir para o primeiro andar!')
# elif idade >= 18 and tipo_ingresso == 'PISTA':
#     print("Pode seguir para a pista!")
# else:
#     print('Você não pode entrar na festa')
#
# print('--- Fim do programa ---')

# Estrutura aninhada
if 17 < idade < 100:
    print('Você pode ir so guichê!')
    tipo_ingresso = input('Digite o tipo ingresso VIP ou PISTA: ')
    tipo_ingresso = tipo_ingresso.upper()
    print(f'Meu tipo de ingresso é {tipo_ingresso}')

    if tipo_ingresso == 'VIP':
        print('Pode seguir para o PRIMEIRO ANDAR!')
    elif tipo_ingresso == 'PISTA':
        print('Vá em direção a PISTA!')
    else:
        print('Seu ingresso não é válido!')

