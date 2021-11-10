"""Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve
 ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que
  o número do canal e o nível do volume permanecem dentro de faixas válidas."""

class Televisão:
    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume


    def DiminuirVolume(self):
        if self.volume == 0:
            print("Não é possível diminuir o volume. Volume = 0")
        
        else:   
            self.volume = self.volume - 10
            print(f"O volume foi diminuido para: {self.volume}")
            

    def AumentarVolume(self):
        if self.volume == 100:
            print("Não é possível aumentar o volume. Volume = 100")
        
        else:   
            self.volume = self.volume + 10
            print(f"O volume foi aumentado para: {self.volume}")


    def TrocarCanal(self, novo_canal):
        if novo_canal >= 50 or novo_canal == 0:
            print("Canal inválido.")

        else:
            self.canal = novo_canal
            print(f"O canal foi alterado para: {novo_canal}")


televisao1 = Televisão(10, 0)
televisao1.DiminuirVolume()
televisao1.AumentarVolume()

televisao2 = Televisão(10, 100)
televisao2.AumentarVolume()

televisao3 = Televisão(10, 50)
televisao3.TrocarCanal(0)
televisao3.TrocarCanal(50)
televisao3.TrocarCanal(20)


        
