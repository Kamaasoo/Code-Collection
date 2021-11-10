"""Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos:
comer(), verBucho() e digerir().
Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos diferentes e
verificando o conteúdo do estomago a cada refeição."""

class Macaco:
    def __init__(self, nome, bucho):
        self.nome = nome
        self.alimentos = [bucho]
        self.bucho = False


    def Comer(self, alimento):
        print(f"{self.nome} comeu: {alimento}")
        self.alimentos.append(alimento)
        self.bucho = False

    def Digerir(self):
        print(f"O alimento foi digerido.")
        self.bucho = True

    def VerBucho(self):
        if self.bucho:
            print(f"Bucho de {self.nome}: {self.alimentos}")

        else:
            print("O alimento ainda não foi digerido.")


macaco1 = Macaco("Jorge", "suco")
macaco2 = Macaco("Pedrin", "Água")

macaco1.Comer(macaco2)
macaco1.Digerir()
macaco1.VerBucho()

