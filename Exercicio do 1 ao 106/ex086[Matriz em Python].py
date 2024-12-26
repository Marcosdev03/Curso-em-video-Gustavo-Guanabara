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
