
maior_peso = 0
menor_peso = 0

for pessoas in range (1,6):
    peso = float(input('Digite o peso da {} pessoa:'.format(pessoas)))

    if pessoas == 1:
        menor_peso = peso
        maior_peso = peso

    if peso > maior_peso:
        maior_peso = peso

    if peso < menor_peso:
        menor_peso = peso
print('O menor peso é:{}Kg'.format(menor_peso))
print('E o maior peso é:{}Kg'.format(maior_peso))



