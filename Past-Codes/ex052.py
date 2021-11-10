num = int(input('Digite um valor: '))
lacrei =  0
for monke in range(1,num +1):
    if num % monke == 0:
        print('\033[132m',end=(' '))
        lacrei += 1
    else:
        print('\033[131m',end=(' '))
    print('{}'.format(monke),end=(' '))
print('\nnúmero {} foi dividido {} vezes!'.format(num,lacrei))
if lacrei == 2:
    print('O número {}, é primo!'.format(num))
else:
    print('O número {}, não é primo!'.format(num))