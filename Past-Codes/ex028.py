from random import randint
from time import sleep

computador = randint(1,5)

resposta = int(input('\033[1:34mDigite o número que estou pensando (de 1 a 5):'))

print('\033[1:34mEstou processando...')
sleep(0.5)
if resposta == computador:
    print('\033[1:34mParabéns você acertou, a resposta era:{}!'.format(resposta))
else:
    print('\033[1:34mVocê perdeu, o número que pensei foi:{}!'.format(computador))
