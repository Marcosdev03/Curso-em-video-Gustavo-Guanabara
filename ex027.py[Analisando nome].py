# Lê o nome completo do usuário
nome_completo = input('Digite seu nome completo: ').strip()

# Divide o nome em partes
nomes = nome_completo.split()

# Obtém o primeiro e o último nome
primeiro_nome = nomes[0]
ultimo_nome = nomes[-1]

# Exibe os resultados
print(f'Primeiro nome: {primeiro_nome}')
print(f'Último nome: {ultimo_nome}')
