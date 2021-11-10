from datetime import date
print('1| Digite um ano ou \n'
      '2| Digite 0 para ver seu ano atual.')
ano = int(input('Digite um ano: '))



if ano == 0:
    print(date.today().year)

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))