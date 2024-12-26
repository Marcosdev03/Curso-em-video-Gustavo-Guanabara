from datetime import date
pessoa = dict()
ano_atual = date.today().year


pessoa['nome'] = str(input('Nome: '))
pessoa['ano nascimento'] = int(input('Ano nascimento: '))
pessoa['carteira de trabalho'] = int(input('Carteira de trabalho (0 não tem): '))
if pessoa['carteira de trabalho'] == 0:
    print('-='*20)
    print(f'- Nome tem o valor {pessoa["nome"]}.')
    idade = date.today().year - pessoa['ano nascimento']
    print(f'- Idade tem o valor {idade}.')
    print(f'- CTPS tem o valor {pessoa["carteira de trabalho"]}.')
    exit()
else:
    pessoa['ano contratação'] = int(input('Ano da contratação: '))
    pessoa['salário'] = float(input('Salário: ').replace(',','.'))
    print('-='*20)
    idade = ano_atual - pessoa['ano nascimento']
    pessoa['idade'] = idade
    anos_trabalhados = ano_atual - pessoa['ano contratação']
    anos_para_aposentadoria = 35 - anos_trabalhados
    idade_aposentadoria = pessoa['idade'] + anos_para_aposentadoria
    pessoa['anos trabalhados'] = anos_trabalhados
    pessoa['idade aposentadoria'] = idade_aposentadoria
    for k ,v in pessoa.items():
     print(f'- {k} tem o valor {v}.')
    





