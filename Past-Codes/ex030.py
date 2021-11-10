numero = int(input('Digite um número: '))

soma = numero % 2

if soma == 0:
    print('O número {}, é par!'.format(numero))
else:
    print('O número {}, é impar!'.format(numero))