from random import randint

def sorteia():
    for c in range(1,6):
        sorteados = randint(1,50)
        sort.append(sorteados)
    return sort
sort = []

print(f'Os números sorteados foram {sorteia()}.')

def somapar():
    soma = 0
    pares = []
    for item in sort:
        if item % 2 == 0:
            soma += item
            pares.append(item)
    return f'A soma dos pares {pares} é {soma}'
    
    
print(somapar())