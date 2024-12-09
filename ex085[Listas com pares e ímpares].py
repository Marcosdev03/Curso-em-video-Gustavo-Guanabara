pares = []
impares = []

for _ in range(7):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        pares.append(num)  # Adiciona aos pares
    else:
        impares.append(num)  # Adiciona aos ímpares

# Ordenando as listas
pares.sort()
impares.sort()

# Exibindo os resultados
print(f'\nValores pares em ordem crescente: {pares}')
print(f'Valores ímpares em ordem crescente: {impares}')
