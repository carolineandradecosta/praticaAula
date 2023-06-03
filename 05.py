import math
def calcula_area_cilindro(raio: float, altura:float):
    PI = 3.14
    area_lateral = (2 * PI * raio * altura)
    area_base = PI * (raio ** 2)
    area_cilindro = area_base + area_lateral

    return area_cilindro


area_cilindro = calcula_area_cilindro(5.0, 20.0)

def calcula_litros(area_cilindro: float):
    qtd_total_litros = area_cilindro / 3
    qtd_latas = math.ceil(qtd_total_litros / 5)
    custo = qtd_latas * 50.0
    return custo

print(calcula_litros(area_cilindro))
