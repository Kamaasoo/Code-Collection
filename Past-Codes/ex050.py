soma = 0
cont = 0

for monke in range(1,7):
    num = int(input('Digite um valor:'))
    if num % 2 == 0:
        soma += monke
        cont += 1
print('O valor de números pares é:{} \n A soma dos números pares é:{}'.format(cont,soma))