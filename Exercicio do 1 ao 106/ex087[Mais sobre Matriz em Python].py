matriz = []

# Preencher a matriz 3x3 com valores lidos pelo teclado
for i in range(3):
    linha = []
    for j in range(3):
        valor = int(input(f'Digite o valor para a posição [{i},{j}]: '))
        linha.append(valor)
    matriz.append(linha)

# Exibir a matriz formatada
print('\nMatriz 3x3:')
for linha in matriz:
    for valor in linha:
        print(f'{valor:4}', end='')  # Formatação para alinhar os valores
    print()  # Quebra de linha após cada linha da matriz

# A) A soma de todos os valores pares
soma_pares = 0
for linha in matriz:
    for valor in linha:
        if valor % 2 == 0:
            soma_pares += valor

# B) A soma dos valores da terceira coluna
soma_coluna_terceira = sum(matriz[i][2] for i in range(3))

# C) O maior valor da segunda linha
maior_segunda_linha = max(matriz[1])

# Exibir os resultados finais
print(f'\nA) A soma de todos os valores pares digitados é {soma_pares}.')
print(f'B) A soma dos valores da terceira coluna é {soma_coluna_terceira}.')
print(f'C) O maior valor da segunda linha é {maior_segunda_linha}.')
