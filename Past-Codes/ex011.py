largur = float(input('Digite a largura da parede: '))
altura = float(input('Agora digite sua altura: '))

m2 = largur * altura
litros = m2 / 2

print('Largura - {} x {} Altura - Sua area é de {:.3f}m2'.format(largur,altura,m2))
print('Será necessário: {}l para pintar: {}m2.'.format(litros,m2))