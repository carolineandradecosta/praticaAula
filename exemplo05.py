# o 'w' foi feito pra escrever eou sobrescrever se já existir o arquivos txt
# nesse caso o 'meu_arquivo.txt foi criado sozinho
with open('meu_arquivo.txt', 'w', encoding='utf-8') as fo:
    fo.write('Eu amo programar em Python\n')
    fo.write('Programar e, SQL é muito bom\n')
    fo.write('Java sempre foi pesado\n')

# o 'a' adicionar conteudos ao arquivo txt se já existir o arquivo
with open('meu_arquivo.txt', 'a', encoding='utf-8') as fo:
    fo.write('Eu amo programar em Python\n')
    fo.write('Programar e, SQL é muito bom\n')
    fo.write('Java sempre foi pesado\n')