from datetime import date

atual = date.today().year
nascimento = int(input('Em qual ano você nasceu?:'))
anos = atual - nascimento

print('Quem nasceu em {} tem {} anos!'.format(nascimento, anos))

if anos == 18:
    print('\033[31mVocê deverá se alistar esse ano!')

elif anos > 18:
    lol = anos - 18
    print('Você deveria ter se alistado há {} anos!'.format(lol))

elif anos < 18:
    lol = 18 - anos
    print('Você deverá se alistar em {} anos.'.format(lol))
