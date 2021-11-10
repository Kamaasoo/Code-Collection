print('Casas Bahianaskkk')

preco = float(input('Digite o preço da sua compra:R$'))
print('A forma de pagamento será?')
print('[ 1 ] À vista (Dinheiro,cheque)')
print('[ 2 ] À vista (Cartão)')
print('[ 3 ] Parcelado cartão 2x')
print('[ 4 ] Parcelado cartão 3x(Ou mais)')

escolha = int(input('Digite o número da sua opção:'))

if escolha == 1:
    desconto_1 = preco - (preco * 10 / 100)
    print('O valor da sua compra será de:R${:.2f}!'.format(desconto_1))

elif escolha == 2:
    desconto_2 = preco - (preco * 5 / 100)
    print('O valor da sua compra será de:R${:.2f}!'.format(desconto_2))

elif escolha == 3:
    print('O valor da sua compra será de:R${:.2f}!'.format(preco))

elif escolha == 4:
    quantidade_parcelas = int(input('Qual será a quantidade de parcelas?:'))
    juros = preco + (preco * 20 / 100)
    precocomjuros = preco + juros
    print('O valor final da compra será de:R${:.2f}'.format(precocomjuros))


