from ex110 import moeda


p = float(input('Digite o preço: '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}.')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}.')
print(f'Aumentando 10% de {p} vai ficar {moeda.moeda(moeda.aumentar(p, 10))}')