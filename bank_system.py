bar = '-' * 40
print('\033[1mBDB - International bank')
print(bar)

while option != 3:
    print('Choose an option:\n[ 0 ] Withdrawal\n [ 1 ] Transfer\n[ 2 ] Deposit\n[ 3 ] Exit')
    option = int(input('Your choise: '))
    
    if option == 0:
        withdramt = int(input('Withdrawal value: R$ '))
        print(bar)

        for cell in [200, 100, 50, 20, 10, 1]:
            amount = withdramt // cell
            withdramt = withdramt % cell

            if amount > 0:
                print(f'R${withdramt} Have been removed from your account.')
                print(f'{amount} cells R$ {cell}\n{bar}')

    if option == 1:
        print(bar)
        tranfsamount = int(input('Transfer amount: R$'))
        account = input('inform the account:'))
        print(f'{tranfsamount} Were transferred to: {account}.\n{bar}')

    if option == 2:
        print(bar)
        depamount = int(input('Deposit value: '))
        print(f'R${depamount} were deposited in your account.\n{bar}')

if option == 3:
    print(f'{bar}\nBDB - Thank you. Check back often!\n{bar}')
