from datetime import date
nascimen = int(input('Digite o seu ano de nascimento: '))

idade = date.today().year - nascimen

print('A sua idade é de {} anos.'.format(idade))

if idade < 9:
    print('\033[32mVocê é um atleta de categoria Mirim!')

elif idade > 9 and idade < 14:
    print('\033[32mVocê é um atleta de categoria Infantil!')

elif idade > 14 and idade < 19:
    print('\033[32mVocê é um atleta de categoria Júnior!')

elif idade > 19 and idade < 25:
    print('\033[32mVocê é um atleta de categoria Sênior!')

elif idade > 25 and idade < 85:
    print('\033[32mVocê é um atleta de categoria Mâster!')

elif idade > 85:
    print('\033[31mOpção inválida!')

