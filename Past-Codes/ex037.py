from time import sleep
número = int(input('Digite um número:'))
sleep(1)
print('1 |Digite 1 para converter esse número em: Binário.')
print('2 |Digite 2 para converter esse número em: Octal.')
print('3 |Digite 3 para converter esse número em: Hexadécimal.')

opção = int(input('Sua escolha:'))

if opção == 1:
    print('\033[32m{} Convertido em binário será:{}'.format(número,bin(número)[2:]))
if opção == 2:
    print('\033[32m{} Convertido em binário será:{}'.format(número, oct(número)[2:]))
if opção == 3:
    print('\033[32m{} Convertido em binário será:{}'.format(número, hex(número)[2:]))
if opção > 3:
    print('\033[31mOpção inválida!')
