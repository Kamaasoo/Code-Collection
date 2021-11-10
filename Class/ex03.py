"""Crie uma classe que modele um retangulo:
Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
"""
 
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def AlterarValores(self, nova_base, nova_altura):
        print(f"Os novos valores do retangulo são: Base = {nova_base}, Altura = {nova_altura}")
        self.base = nova_base
        self.altura = nova_altura

    def VerValores(self):
        print(f"O valor da base é: {self.base}. O valor de altura é: {self.altura}")

    def CalcularArea(self):
        area = self.base * self.altura
        print(f"A área do retangulo é de: {area}")

    def CalcularPerimetro(self):
        perimetro = self.base * 2 + self.altura * 2 
        print(f"O perímetro é de: {perimetro}")


retangulo1 = Retangulo(4, 8)       
retangulo1.CalcularArea()
retangulo1.CalcularPerimetro()
retangulo1.VerValores()

retangulo1.AlterarValores(5, 7)
retangulo1.CalcularArea()
retangulo1.CalcularPerimetro()

    
