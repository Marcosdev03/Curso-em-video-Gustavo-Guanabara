dados = dict()
lista = []
while True:
 dados['nome'] = str(input('Nome:'))
 dados['sexo'] = str(input('sexo [M]/[F]:')).upper()
 while True:
    if dados['sexo'] not in ['f','F','m','M']:
        print('ERRO!Digite [M] ou [F]')
        dados['sexo'] = str(input('sexo [M]/[F]:')).upper()        
    else:
        break
 dados['idade'] = int(input('Idade: '))
 lista.append(dados.copy())
 resposta = input('Quer continuar? [S] ou [N]:').upper()
 if resposta not in ['S','N']:
     print('ERRO!Digite [S] ou [N]')
     resposta = input('Quer continuar [S] ou [N]:').upper()
 elif resposta == 'N':
     break
 elif resposta == 'S':
     continue
print('-='*30)
print(f'A) Ao todo temos {len(lista)} pessoas cadastradas.')
media = sum(pessoa['idade'] for pessoa in lista) / len(lista)
print(f'B) A média de idade é de {media}.')
num_mulheres = sum(1 for pessoa in lista if pessoa['sexo'] == 'F')
print(f'C) Ao todo, temos {num_mulheres} mulheres cadastrada(S).')
print('Lista de pessoas que estão acima da média:',end='')
print()
for pessoa in lista:
    if pessoa['idade'] > media:
        print(f'nome = {pessoa["nome"]} com {pessoa["idade"]}')
    else:
        print('Nehuma pessoa acima da média!')
        
print('<<ENCERRADO>>')
    