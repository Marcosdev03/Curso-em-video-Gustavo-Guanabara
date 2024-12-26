lista = []

for c in range(1, 6):
    num = float(input(f'Digite o peso da {c}º pessoa: '))
    lista.append(num)
    
print(f'O maior peso é {max(lista)}kg.')
print(f'O menor peso é {min(lista)}kg.')