soma = 0
contagem = 0

for monke in range(1,501, 2):
    if monke % 3 == 0:
        soma += monke
        contagem += 1
print('A soma de {} valores, é de {}!'.format(contagem,soma))
