from math import trunc

numero = float(input("Digite um número real: "))
porcao_inteira = trunc(numero)

print("A porção inteira de {} é {}.".format(numero, porcao_inteira))
