cont = 0
somaidade = 0
média_idade = 0
maior_idade_homem = 0
nome_homem = 0

for pessoas in range (1,5):
    print('\033[1m-----{} Pessoa-----'.format(pessoas))
    nome = str(input('Nome:')).strip()
    idade = int(input('Idade:'))
    sexo =  str(input('Sexo [M/F]:')).strip()

    cont += 0
    somaidade += idade
    média_idade = somaidade / 4

    if pessoas == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_homem = nome

    if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_homem = nome

    if sexo in 'Ff' and idade < 20:
            cont += 1

print('A média de idade do grupo é de: {:.1f} anos!'.format(média_idade))
print('O homem mais velho do grupo tem: {} anos e se chama {}.'.format(maior_idade_homem,nome_homem))
print('A quantidade de mulheres com menos de 20 anos no grupo é:{}!'.format(cont))








