valores = []

for c in range(1, 6):
    num = int(input(f'Digite um valor para a posição {c}: '))
    valores.append(num)
print(f'Você digitou os valores {valores}.')

maior = max(valores)
menor = min(valores)

print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end=' ')

print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end=' ')
