with open('contos_dos_irmaos_grimm.txt', 'r', encoding='utf-8') as fo:
    conteudo = fo.read()
    print(conteudo)

with open('contos_dos_irmaos_grimm.txt', 'r', encoding='utf-8') as fo:
    linhas = fo.readlines()

    contador = 0
    for linha in linhas:
        contador += 1
    print(f'Quantidade de linhas: {contador}')
