def calculadora(n1, n2):
    resultado_soma = n1 + n2
    resultado_sub = n1 - n2
    resultado_mult = n1 * n2
    resultado_divi = n1 / n2

#    return [resultado_soma, resultado_sub, resultado_mult, resultado_divi]
    return resultado_soma, resultado_sub, resultado_mult, resultado_divi

#print(calculadora(10, 20))

soma, subtracao, multiplicacao, divisao = calculadora(10, 20)

print(f'Soma: {soma}')
print(f'Subtraçao: {subtracao}')
print(f'Miltiplicação: {multiplicacao}')
print(f'Divisão: {divisao}')

