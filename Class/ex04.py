""" Crie uma classe que modele uma pessoa:
Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano
 que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""
class Pessoa:
    def __init__ (self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    
    def Envelhecer(self):
        self.idade = self.idade + 1
        print(f"{self.nome} Envelheceu, possuindo {self.idade} anos.")

    def Engordar(self):
        self.peso = self.peso + 1
        print(f"{self.nome} Engordou ganhando 1Kg. Peso = {self.peso}Kg")

    def Emagrecer(self):
        self.peso = self.peso - 1 
        print(f"{self.nome} Emagreceu perdendo 1Kg. Peso = {self.peso}Kg")

    def Crescer(self):
        if self.idade <= 21:
            self.altura =  self.altura + 0.5
            print(f"{self.nome} Cresceu 0,5cm. Altura = {self.altura}m")
        else:
            print(f"{self.nome} Não pode mais crescer pois tem mais de 21 anos. Altura = {self.altura}m")


pessoa1 = Pessoa('Kamaso', 18, 80, 1.75)
pessoa1.Envelhecer()
pessoa1.Crescer()

pessoa2 = Pessoa("Daniel", 22, 80, 1.75)
pessoa2.Crescer()

pessoa2.Engordar()
pessoa2.Emagrecer()



