from math import sin, cos, radians, tan
an = float(input('Digite o valor do angulo: '))

seno = sin(radians(an))
coseno = cos(radians(an))
tangente = tan((radians(an)))
print(' O seno do angulo 30{} é de {:.2f}\n e o seu coseno é {:.2f}'.format(an,seno,coseno))
print('A sua tangente é de {:.2f}'.format(tangente))