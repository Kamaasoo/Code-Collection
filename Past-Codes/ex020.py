import random
aluno1 = (input('Digite o nome do primeiro aluno: '))
aluno2 = (input('Digite o nome do segundo aluno: '))
aluno3 = (input('Digite o nome do terceiro  aluno: '))
aluno4 = (input('Digite o nome do quarto aluno: '))

alunostotal = [aluno1, aluno2,aluno3,aluno4]
random.shuffle(alunostotal)
print('A ordem dos alunos a apresentarem o trabalho será:')
print(alunostotal)