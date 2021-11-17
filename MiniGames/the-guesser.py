#The Guesser

import os
from random import randint

num = randint(0, 50)
tentativa = 0
chute = 0
print('\033[1m-' * 15, 'O adivinhador', '-' * 15)

print('Foi sorteado um número de 0 a 50! \nTente adivinhar qual número foi gerado.')
while chute != num:
	chute = int(input('Qual o seu chute?: '))
	if chute < num:
		os.system('cls')
		print('-' * 40)
		print(f'O valor sorteado é maior que {chute}!')
		tentativa += 1

	if chute > num:
		os.system('cls')
		print('-' * 40)
		print(f'O valor sorteado é menor que {chute}!')
		tentativa += 1

	if chute == num:
		os.system('cls')
		print('-' * 40)
		print(f'Você acertou! O número sorteado foi {num}!')
		print(f'O seu número de tentativas foi de {tentativa}!')
		print('-' * 40)
