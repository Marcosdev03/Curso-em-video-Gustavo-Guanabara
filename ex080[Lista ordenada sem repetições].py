numeros = []

for _ in range(5):
    num = int(input('Digite um valor: '))
    if not numeros or num > numeros[-1]:  # Adicionar no final se for maior que o último
        numeros.append(num)
        print('Adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(numeros):  # Encontrar a posição correta
            if num <= numeros[pos]:
                numeros.insert(pos, num)
                print(f'Adicionado na posição {pos} da lista.')
                break
            pos += 1

print(f'Os valores digitados em ordem foram {numeros}.')
