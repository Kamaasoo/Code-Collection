peso = float(input('Digite o seu peso:(kg)'))
altura = float(input('Digite a sua altura:(m)'))

imc = peso / (altura ** 2)

print('O seu IMC é de {}'.format)

if imc < 18.5:
    print('Você está abaixo do peso!')
elif imc > 18.5 and imc < 25:
    print('O seu peso está ideal!')
elif imc > 25 and imc < 30:
    print('Você está em sobrepeso!')
elif imc > 30 and  imc < 40:
    print('Você está em obesidade!')
elif imc > 40:
    print('Você está em obesidade mórbida!')

