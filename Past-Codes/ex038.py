n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))

maior = n1

if n1 > n2:
    print('\033[1:32mO primeiro número é maior :{}'.format(maior))
elif n1 == n2:
    print('\033[1:32mOs valores são iguais!')
else:
    maior = n2
    print('\033[1:32mO segundo número é maior:{}'.format(maior))
