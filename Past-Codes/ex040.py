
nota1 = float(input('Digite a sua primeira nota:'))
nota2 = float(input('Digite a sua segunda nota:'))

média = (nota1 + nota2) / 2

print('Sua média é de {}!'.format(média))

if média > 7.0:
    print('Você está aprovado.')

elif média < 5.0:
    print('Você está reprovado.')
elif média > 5.0 and média < 6.9:
    print('Você está de recuperação.')

