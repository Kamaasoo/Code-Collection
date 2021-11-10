""" Crie uma classe que modele uma bola:
Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
"""

class Bola:
    def __init__ (self, cor, circuferencia, material):
        self.cor = cor
        self.circuferencia = circuferencia
        self.material = material

    def MostrarCor(self):
        print(f"A cor dessa bola é: {self.cor}")

    def TrocarCor(self, nova_cor):
        print(f"A cor da bola foi alterada para {nova_cor}")
        self.cor = nova_cor
        


Bola1 = Bola('Preto', 20, "Madeira")

Bola1.MostrarCor()
Bola1.TrocarCor("Azul")
Bola1.MostrarCor()
