print('-' * 40)
print('\033[1mBDB - Banco Internacional')
print('-' * 40)

opcao = 0

while opcao != 3:
    print('Escolha uma opção:')
    print('[ 0 ] Saque ')
    print('[ 1 ] Transferência')
    print('[ 2 ] Depósito ')
    print('[ 3 ] Sair')

    opcao = int(input('Digite sua escolha:'))
    if opcao == 0:
        valorSaque = int(input('Valor do saque: R$ '))
        print('-' * 40)

        for nota in [200, 100, 50, 20, 10, 1]:
            quantidade = valorSaque // nota
            valorSaque = valorSaque % nota

            if quantidade > 0:
                print(f'Foram retirados R${valorSaque} da sua conta.')
                print(f'{quantidade} notas de R$ {nota}')
                print('-' * 40)

    if opcao == 1:
        print('-' * 40)
        valorTransf = int(input('Digite o valor que quer transferir: R$'))
        conta = str(input('Digite a conta bancária que deseja transferir:'))
        print(f'Foram transferidos {valorTransf} para a conta {conta}.')
        print('-' * 40)

    if opcao == 2:
        print('-' * 40)
        valorDeposit = int(input('Digite o valor do depósito: R$'))
        print(f'Foram depósitados R${valorDeposit} em sua conta.')
        print('-' * 40)

if opcao == 3:
    print('-' * 40)
    print('BDB - Agradece. Volte sempre!')
    print('-' * 40)


