primeiro = int(input('Digite o primeiro termo da PA:'))
razão = int(input('Digite a razão da PA:'))
termo = primeiro
cont = 1
total = 0
while continuar != 0:
    total = total + continuar
    while cont <= total:
        print('{} '.format(termo), end='')
        termo += razão
        cont += 1
    continuar = int(input('Quantos termos quer mostrar a mais?:'))

