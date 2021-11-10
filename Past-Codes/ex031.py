distan = float(input('Digite a distância da viagem: '))

print ('A viagem será de {}km'.format(distan))

if distan < 200:
    eitakkk = distan * 0.50
    print('O valor da passagem será de:R${:.2f}!'.format(eitakkk))
else:
    eita2x = distan * 0.45
    print('O valor da passagem será de:R${:.2f}!'.format(eita2x))
print('Boa viagem!')
