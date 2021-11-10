salario = float(input('Digite o seu salário atual:R$'))

if salario > 1250:
    calculo = (salario * 10) / 100 + (salario)
    print('O salário será de :R${:.2f}'.format(calculo))
else:
    calculo = (salario * 15) / 100 + (salario)
    print('O salário será de:R${:.2f}'.format(calculo))