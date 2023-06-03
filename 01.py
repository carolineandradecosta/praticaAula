import statistics
lista = [4, 5, 8, 9]
media2= statistics.median(lista)
print(media2)

def calcula_media (n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4) / 4
    print(f'media = {media:0.2f}')

    if media >= 7.0:
        print('Você está aprovado')
    elif 4.0 <  media < 7.0:
        print('Você está de recuperação')
    else:
        print('Você está reprovado')


calcula_media(4.0, 7.0, 6.2, 8.7)


