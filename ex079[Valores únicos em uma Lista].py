numeros = []

while True:
    num = int(input('Digite um valor: '))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar.')
    
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

numeros.sort()
print(f'Você digitou os valores {numeros}')
