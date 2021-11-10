print('10 termos de uma PA!')
termo = int(input('Digite o primeiro termo:'))
razão = int(input('Digite a razão:'))
décimo_termo = termo + (10 - 1) * razão

for monke in range(termo,décimo_termo + razão,razão):
    print(monke, end=' ')