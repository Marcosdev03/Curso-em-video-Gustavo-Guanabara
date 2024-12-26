from datetime import date
idade_pessoas = []
maior_idade = []
menor_idade = []


for c in range(1, 8):
    ano_nascimento = int(input(f'Digite o ano de nascimento da {c}º pessoa: '))
    idade = date.today().year - ano_nascimento
    idade_pessoas.append(ano_nascimento)
    if idade >= 18:
     maior_idade.append(ano_nascimento)
    else:
        menor_idade.append(ano_nascimento)
     
print(f'Ao total tivemos {len(maior_idade)} pessoas maiores de idade.')
print(f'E também tivemos {len(menor_idade)} menores de idade.')