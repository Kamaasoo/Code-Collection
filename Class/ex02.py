""" Crie uma classe que modele um quadrado:
Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""
class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def RetornarLado(self):
        print(f"O valor do lado é de: {self.lado}")

    def TrocarLado(self, novo_lado):
        print(f" O novo valor do lado é: {novo_lado}")
        self.lado = novo_lado

    def CalcularArea(self):
        Area = self.lado * self.lado
        print(f"O valor da área é de {Area}")


quadrado1 = Quadrado(8)

quadrado1.RetornarLado()
quadrado1.CalcularArea()

quadrado1.TrocarLado(4)
quadrado1.CalcularArea()
