sexo = str(input('Digite o seu sexo[M/F]:')).strip().upper()

while sexo not in 'MmFf':
    print('Dado inválido digite novamente.')
    sexo = str(input('Digite o seu sexo[M/F]:')).strip().upper()

print('\033[32mSexo {} registrado!'.format(sexo))