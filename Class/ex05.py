"""Crie uma classe para implementar uma conta corrente. A classe deve
possuir os seguintes atributos: número da conta, nome do correntista e saldo. Os métodos são os
seguintes: alterarNome, depósito e saque"""

class ContaCorrente:
    def __init__ (self, conta, nome, saldo):
        self.conta = conta
        self.nome = nome
        self.saldo = saldo

    def AlterarNome(self, novo_nome):
        print(f"{self.nome} O nome da conta foi alterado para: {novo_nome}")
        self.nome = novo_nome

    def Deposito(self,valor_deposito):
        print(f"O valor de: R${valor_deposito}, foi atribuido a sua conta.")
        self.saldo = self.saldo + valor_deposito

    def Saque(self,valor_saque):
        print(f"Foi retirado: R${valor_saque} Da sua conta.")
        self.saldo = self.saldo - valor_saque

    def ConsultarSaldo(self):
        print(f"Você possui: R${self.saldo} na sua conta.")


conta1 = ContaCorrente("0120012010", "Kamaso", 200)

conta1.ConsultarSaldo()
conta1.Saque(100)
conta1.ConsultarSaldo()
conta1.Deposito(300)
conta1.ConsultarSaldo()
conta1.AlterarNome("Kmsz")


            
