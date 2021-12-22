largur = float(input('Digite a largura da parede: '))
altura = float(input('Agora digite sua altura: '))

m2 = largur * altura
litros = m2 / 2

print(f'Largura - {largur} x {altura} Altura - Sua area é de {m2:.3f}m2')
print(f'Será necessário: {litros}l para pintar: {m2}m2.')
