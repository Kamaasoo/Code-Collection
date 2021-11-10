fodase = str(input('Digite o seu nome: ')).strip()

nomelis = fodase.split()
print('O seu primeiro nome é: {}'.format(nomelis[0]))
print('O seu último nome é: {}'.format(nomelis[len(nomelis)-1]))
