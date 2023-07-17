class Personagem:
    def __init__(self, nome, pontuacao, moedas):
        self.nome = nome
        self.pontuacao = pontuacao
        self.moedas = moedas

    def usar_poder(self):
        if self.nome == "Mario":
            return "Super Mario"
        elif self.nome == "Luige":
            return "Fire Luigi!"
        else:
            return "Flying Yoshi!"


personagem1 = Personagem("Mario", 25, 5)
personagem2 = Personagem("Luige", 10, 25)
personagem3 = Personagem("Yoshi", 15, 45)

print(f'Nome do personagem: {personagem2.nome} Poder Especial: {personagem2.usar_poder()} Pontuação: {personagem2.pontuacao} Moedas: {personagem2.moedas}')
