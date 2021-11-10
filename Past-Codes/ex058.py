from random import randint

computador = randint(1,10)
jogador = 0
cont = 0
print('Estou pensando em um número de 1 a 10! Consegue adivinha-lo?')

while jogador != computador:
    jogador = int(input('Digite a sua escolha:'))

    if jogador > computador:
        print('O número é menor!')
        cont += 1
    if jogador < computador:
        print('O número é maior!')
        cont += 1
    if jogador == computador:
        print('Você venceu!')
        cont += 1
print('O número em que pensei foi {}!'.format(computador))
print('Você acertou com o total de {} tentativas.'.format(cont))






