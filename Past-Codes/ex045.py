from time import sleep
from random import randint

itens = ('pedra','papel','tesoura')
computador = randint(0,2)
print('JoKenPo!')
print('[ 0 ] Pedra')
print('[ 1 ] Papel')
print('[ 2 ] Tesoura')
escolha = int(input('Escolha um:'))

print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po!')
sleep(1)

print('O computador escolheu:{}'.format(itens[computador]))
print('O jogador escolheu:{}'.format(itens[escolha]))
if computador == 0: #computado jogou pedra!
    if escolha == 0:
        print('\033[34mO jogador e a máquina escolheram: Pedra! Empate.')

    elif escolha == 1:
        print('\033[32mO jogador venceu!')

    elif escolha == 2:
       print('\033[31mO jogador perdeu!')

    else:
        print('\033[31mEscolha inválida!')

if computador == 1: #computador jogou papel!
    if escolha == 0:
        print('\033[31mO jogador perdeu!')

    elif escolha == 1:
        print('\033[34mO jogador e a máquina escolheram: Papel! Empate.')

    elif escolha == 2:
       print('\033[31mO jogador perdeu!')

    else:
        print('\033[31mEscolha inválida!')

if computador == 2: #computdor jogou tesoura!
    if escolha == 0:
        print('\033[32mO jogador venceu!')

    elif escolha == 1:
        print('\033[31mO jogador perdeu!')

    elif escolha == 2:
        print('\033[34mO jogador e a máquina escolheram: Tesoura! Empate.')

    else:
        print('\033[31mEscolha inválida!')
