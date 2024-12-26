# Inicializando as variáveis
nomes = []
idades = []
sexos = []
soma_idades = 0
nome_homem_mais_velho = ""
idade_homem_mais_velho = 0
mulheres_menores_20 = 0

# Coletando dados de 4 pessoas
for i in range(1, 5):
    print(f'{"=" * 7} {i}ª PESSOA {"=" * 7}')
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip().upper()
    
    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)
    
    soma_idades += idade
    
    # Verificando o homem mais velho
    if sexo == 'M' and (idade > idade_homem_mais_velho):
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    
    # Contando mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheres_menores_20 += 1

# Calculando a média de idade
media_idade = soma_idades / 4

# Exibindo os resultados
print(f'\n{"=" * 20}')
print(f'A média de idade do grupo é de {media_idade:.2f} anos.')
if nome_homem_mais_velho:
    print(f'O homem mais velho é {nome_homem_mais_velho} com {idade_homem_mais_velho} anos.')
else:
    print('Não há homens no grupo.')
print(f'Ao todo são {mulheres_menores_20} mulheres com menos de 20 anos.')
