# Lista para armazenar os dados dos alunos
boletim = []

# Função para calcular a média
def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

# Perguntar quantos alunos serão cadastrados
while True:
    try:
        quantidade = int(input('Quantos alunos você deseja cadastrar? '))
        if quantidade > 0:
            break
        else:
            print("Por favor, insira um número válido de alunos.")
    except ValueError:
        print("Por favor, insira um número inteiro válido.")

# Cadastrar os dados dos alunos
for _ in range(quantidade):
    nome = input('\nDigite o nome do aluno: ')
    while True:
        try:
            nota1 = float(input(f'Digite a primeira nota de {nome}: '))
            nota2 = float(input(f'Digite a segunda nota de {nome}: '))
            break
        except ValueError:
            print("Por favor, insira uma nota válida.")

    media = calcular_media(nota1, nota2)
    boletim.append([nome, nota1, nota2, media])

# Exibir o boletim com as médias
print('\nBoletim:')
print('-' * 40)
for aluno in boletim:
    print(f'Nome: {aluno[0]} | Nota 1: {aluno[1]} | Nota 2: {aluno[2]} | Média: {aluno[3]:.2f}')
print('-' * 40)

# Consultar notas de um aluno específico
while True:
    nome_consulta = input('\nDigite o nome do aluno para ver suas notas (ou "sair" para encerrar): ').strip()
    if nome_consulta.lower() == 'sair':
        break
    aluno_encontrado = False
    for aluno in boletim:
        if aluno[0].lower() == nome_consulta.lower():
            aluno_encontrado = True
            print(f'Notas de {aluno[0]}: Nota 1 = {aluno[1]} | Nota 2 = {aluno[2]} | Média = {aluno[3]:.2f}')
            break
    if not aluno_encontrado:
        print(f'Aluno {nome_consulta} não encontrado.')
