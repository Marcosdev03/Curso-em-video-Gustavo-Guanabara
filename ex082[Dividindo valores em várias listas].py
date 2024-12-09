numeros = []
pares = []
impares = []

while True:
    num = int(input('Digite um número: '))
    numeros.append(num)

    if num % 2 == 0:
        pares.append(num)  # Adiciona aos pares
    else:
        impares.append(num)  # Adiciona aos ímpares

    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print(f'\nA lista completa é: {numeros}')
print(f'A lista de números pares é: {pares}')
print(f'A lista de números ímpares é: {impares}')
