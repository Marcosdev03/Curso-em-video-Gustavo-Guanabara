import random

# Função para gerar um único jogo com 6 números aleatórios entre 1 e 60
def gerar_jogo():
    return random.sample(range(1, 61), 6)

# Lista para armazenar os jogos gerados
jogos = []

# Perguntar quantos jogos o usuário deseja gerar
quantidade = int(input('Quantos jogos você deseja gerar? '))

# Gerar os jogos
for _ in range(quantidade):
    jogos.append(gerar_jogo())

# Exibir os jogos gerados
print(f'\nSorteando {quantidade} jogos:')
for i, jogo in enumerate(jogos, 1):
    print(f'Jogo {i}: {sorted(jogo)}')
