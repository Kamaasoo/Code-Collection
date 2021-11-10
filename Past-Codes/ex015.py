dias = int(input('Por quantos dias você utilizou o veiculo?: '))
kms = float(input('Quantos kilômetros rodou?: '))

somadias = dias * 60
somakms = kms * 0.15
somatotal = somakms + somadias

print('O total do aluguel será de:R${:.2f}'.format(somatotal))