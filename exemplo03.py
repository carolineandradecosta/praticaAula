# O for é importante porque permite manipulações, já que a nálise é feita linha a linha
# Pulando linha
with open('arquivo.txt', 'r', encoding='utf-8') as fo:
    for linha in fo:
        print(linha)

# Sem pular linha
with open('arquivo.txt', 'r', encoding='utf-8') as fo:
    for linha in fo:
        print(linha.rstrip())

with open('arquivo.txt', 'r', encoding='utf-8') as fo:
    for linha in fo:
        if 'M' in linha:
            print(f'Tipo:{type(linha)} | {linha}')
