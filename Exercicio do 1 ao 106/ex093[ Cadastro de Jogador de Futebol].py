jogador = dict()
jogador["nome"] = str(input('Nome do jogador: '))
jogador["partidas"] = int(input(f'Quantas partidas {jogador["nome"]} jogou:'))
jogador["gols"] = []
jogador["total"] = []
for c in range(jogador["partidas"]):
  gols = int(input(f'  Quantos gols na partida {c + 1}: '))
  jogador["gols"].append(gols)
  total = sum(jogador["gols"])
  jogador["total"] = total
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas.')

for c in range(jogador["partidas"]):
     print(f'=> Na partida {c + 1}, fez {jogador["gols"][c]} gols.')
print(f'O jogador jogou {total} partida(s).')
jogadores = []

while True:
    jogador = dict()
    
    # Coleta informações do jogador
    jogador["nome"] = str(input('Nome do jogador: '))
    jogador["partidas"] = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
    jogador["gols"] = []
    
    # Coleta os gols de cada partida
    for c in range(jogador["partidas"]):
        gols = int(input(f'  Quantos gols na partida {c + 1}: '))
        jogador["gols"].append(gols)
    
    jogador["total"] = sum(jogador["gols"])  # Total de gols
    jogadores.append(jogador)
    
    # Pergunta se deseja continuar com outro jogador
    resposta = input('Quer cadastrar outro jogador? [S/N]: ').upper()
    if resposta == 'N':
        break

# Exibe informações de todos os jogadores
print('-=' * 30)
for jogador in jogadores:
    print(f'Informações do jogador {jogador["nome"]}:')
    print(f'Jogou {jogador["partidas"]} partidas.')
    
    for c in range(jogador["partidas"]):
        print(f'=> Na partida {c + 1}, fez {jogador["gols"][c]} gols.')
    
    print(f'O total de gols do jogador {jogador["nome"]} foi {jogador["total"]}.')
    print('-=' * 30)

# Exibe um resumo de todos os jogadores
print('Resumo de todos os jogadores:')
for jogador in jogadores:
    print(f'O jogador {jogador["nome"]} jogou {jogador["partidas"]} partidas e fez um total de {jogador["total"]} gols.')
