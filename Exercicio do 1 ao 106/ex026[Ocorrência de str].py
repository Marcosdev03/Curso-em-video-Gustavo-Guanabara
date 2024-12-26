# Lê uma frase do usuário
frase = input('Digite uma frase: ').strip().upper()  # Converte para maiúsculas para uniformidade

# Conta quantas vezes a letra 'A' aparece
contador_a = frase.count('A')

# Encontra a posição da primeira e última ocorrência de 'A'
primeira_ocorrencia = frase.find('A')
ultima_ocorrencia = frase.rfind('A')

# Exibe os resultados
print(f'A letra "A" aparece {contador_a} vezes.')
if contador_a > 0:
    print(f'A primeira ocorrência de "A" está na posição: {primeira_ocorrencia + 1}')  # +1 para tornar a posição mais amigável
    print(f'A última ocorrência de "A" está na posição: {ultima_ocorrencia + 1}')  # +1 para tornar a posição mais amigável
