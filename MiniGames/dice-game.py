#Dice game
from random import choice

print('-' * 40)
print('\033[1:34m Simulador de dado')
print('-' * 40)

escolha = 0
valores = choice([1,2,3,4,5,6])
valores2 = choice([1,2,3,4,5,6])

while escolha != 1:
    print('[ 0 ] Jogar os dados \n[ 1 ] Sair ')
    escolha = int(input('Digite sua opção:'))
    print('-' * 40)

    if escolha == 0:
        print('[ 0 ] Jogar 1 dado \n[ 1 ] Jogar 2 dados')
        escolha2 = int(input('Digite sua opção:'))
        print('-' * 40)
        if escolha2 == 1:
            print(f'O valor do primeiro dado foi: {valores} e do segundo dado foi: {valores2}!')
        if escolha2 == 0:
            print(f'O valor do dado foi de {valores}')
