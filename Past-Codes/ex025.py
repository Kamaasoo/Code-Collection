nome = str(input('Digite qual o seu nome: '))

minus = nome.lower()
espa = minus.strip()

print('O seu nome tem silva?:{}'.format('silva' in espa))