aluno = dict()

aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print('-='*20)
print(f'-O nome é igual a {aluno['nome']}')
print(f'-A média é igual a {aluno['media']}')
if aluno['media'] >= 7:
    aluno["situação"] = 'aprovado'
elif  5 <=  aluno['media'] <= 7:
    aluno["situação"] = 'recuperação'
else:
    aluno["situação"] = 'reprovado'
    
print(f'-A situação do {aluno['nome']} é {aluno['situação']}.')
