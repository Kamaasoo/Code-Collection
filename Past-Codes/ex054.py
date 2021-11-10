from datetime import date
ano = date.today().year

cont_maior = 0
cont_menor = 0

for monke in range(1,8):
    nascimento = int(input('Digite a {} data de nascimento: '.format(monke)))
    idade = ano - nascimento

    if idade >= 21:
        cont_maior += 1

    elif idade < 21:
        cont_menor += 1
        
print('A quantidade de pessoas menores de idade é: {}!'.format(cont_menor))
print('A quantidade de pessoas maiores de idade é: {} pessoas!'.format(cont_maior))
