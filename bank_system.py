bar = '-' * 40
print('\033[1mBDB - International bank')
print(bar)

while option != 3:
    print('Escolha uma opção:\n[ 0 ] Saque\n [ 1 ] Transferência\n[ 2 ] Depósito\n[ 3 ] Sair')
    option = int(input('Digite sua escolha:'))
    
    if option == 0:
        withdramt = int(input('Valor do saque: R$ '))
        print(bar)

        for cell in [200, 100, 50, 20, 10, 1]:
            amount = withdramt // cell
            withdramt = withdramt % cell

            if quantidade > 0:
                print(f'R${withdramt} Have been removed from your account.')
                print(f'{amount} cells R$ {cell}\n{bar}')

    if option == 1:
        print(bar)
        tranfsamount = int(input('Transfer amount: R$'))
        account = input('inform the account:'))
        print(f'{tranfsamount} Were transferred to: {account}.\n{bar}')

    if option == 2:
        print(bar)
        depamount = int(input('Deposit value: ))
        print(f'Foram depósitados R${depamount} em sua conta.\n{bar}')

if option == 3:
    print(f'{bar}\nBDB - Agradece. Volte sempre!\n{bar}')
