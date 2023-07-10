print('--- Iniciando o Programa ---')

op = input('Digite 0 sem permissão ou 1 com permissão: ')

# 1 representa pessoas com permissão e 0 pessoas sem permissão
# o for com o if vai fazer um filtro, conforme escolha da opção
# o linha[0] representa o primeiro elemento
# o linha[2:] vai imprimir a partir da posição 2 até o fim
with open('arquivo03.txt', 'r', encoding='utf-8') as fo:
    for linha in fo:
        if linha[0] == op:
            print(linha[2:].rstrip())