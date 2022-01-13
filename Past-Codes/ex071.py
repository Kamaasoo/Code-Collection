bars = '-' * 40

print(bars)
print('\033[1mBDB - Banco Internacional')
print(bars)

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
        print(bars)

        for nota in [200, 100, 50, 20, 10, 1]:
            quantidade = valorSaque // nota
            valorSaque = valorSaque % nota

            if quantidade > 0:
                print(f'Foram retirados R${valorSaque} da sua conta.')
                print(f'{quantidade} notas de R$ {nota}')
                print(bars)

    if opcao == 1:
        print(bars)
        valorTransf = int(input('Digite o valor que quer transferir: R$'))
        conta = str(input('Digite a conta bancária que deseja transferir:'))
        print(f'Foram transferidos {valorTransf} para a conta {conta}.')
        print(bars)

    if opcao == 2:
        print(bars)
        valorDeposit = int(input('Digite o valor do depósito: R$'))
        print(f'Foram depósitados R${valorDeposit} em sua conta.')
        print(bars)

if opcao == 3:
    print(bars)
    print('BDB - Agradece. Volte sempre!')
    print(bars)


