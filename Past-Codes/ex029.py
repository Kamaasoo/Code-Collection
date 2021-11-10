velocit = float(input('Digite a sua velociade:  '))
if velocit > 80:
    print('Você foi multado! O limite é de 80km/h.')
    multa = (velocit-80) * 7
    print('O valor da multa foi:R${:.2f}!'.format(multa))
print('Dirija com segurança!')