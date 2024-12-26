pessoas = []

while True:
    nome = input('Digite o nome: ')
    peso = float(input('Digite o peso: '))
    pessoas.append([nome, peso])

    continuar = input('Quer continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

# A) Quantas pessoas foram cadastradas
total_pessoas = len(pessoas)

# B) Pessoas mais pesadas
maior_peso = max(peso for _, peso in pessoas)
mais_pesadas = [nome for nome, peso in pessoas if peso == maior_peso]

# C) Pessoas mais leves
menor_peso = min(peso for _, peso in pessoas)
mais_leves = [nome for nome, peso in pessoas if peso == menor_peso]

print(f'\nA) Total de pessoas cadastradas: {total_pessoas}')
print(f'B) Pessoas mais pesadas: {", ".join(mais_pesadas)} com {maior_peso}kg')
print(f'C) Pessoas mais leves: {", ".join(mais_leves)} com {menor_peso}kg')
