from time import sleep
casa = float(input('digite o valor da sua casa:R$'))
salario = float(input('digite o valor do seu salário:R$'))
anos = int(input('digite em quantos anos você quer parcelar:'))

preço = casa / (anos * 12)
porcent_salario = salario * 30 / 100
print('\033[1:31mProcessando... Por favor aguarde.')
sleep(2)
print('A casa será parcelada em {}'.format(anos))
print('As prestações serão de:R${:.2f}'.format(preço))

if preço > porcent_salario:
    print('\033[1:31mVocê não tem condições de financiar essa casa!')
    print('\033[1:31mEmpréstimo NEGADO!')
else:
    print('\033[1:32mVocê conseguirá pagar essa casa!')
    print('\033[1:32mEmpréstimo concedido!')