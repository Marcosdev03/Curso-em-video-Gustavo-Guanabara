from ex110 import moeda
p = float(input('Digite o preço: '))
print(f'A metade de {p} é {moeda.metade(p)}.')
print(f'O dobro de {p} é {moeda.dobro(p)}.')
print(f'Aumentando 10% de {p} vai ficar {moeda.aumentar(p, 10)}')