frase = str(input('Digite uma frase: ')).upper().strip()

print('A letra "a" aparece {} vezes!'.format(frase.count('A')))
print('A letra "A" aparece na posição {}!'.format(frase.find('A')+1))
print('A letra última letra "a" aparece na posição {}!'.format(frase.rfind('A')))