r1 = float(input('Digite um valor:'))
r2 = float(input('Digite outro valor:'))
r3 = float(input('Digite mais valor:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print("O segmento pode formar um triângulo")
else:
  print("Os segmentos não podem formar um triângulo.")
