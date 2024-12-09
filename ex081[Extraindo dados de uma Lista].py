numeros = []

while True:
    num = int(input('Digite um número: '))
    numeros.append(num)
    
    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

# A) Quantos números foram digitados
quantidade = len(numeros)

# B) Lista ordenada de forma decrescente
numeros_decrescente = sorted(numeros, reverse=True)

# C) Verificar se o valor 5 está na lista
tem_cinco = 5 in numeros

print(f'\nVocê digitou {quantidade} números.')
print(f'A lista de valores em ordem decrescente é {numeros_decrescente}.')
if tem_cinco:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
