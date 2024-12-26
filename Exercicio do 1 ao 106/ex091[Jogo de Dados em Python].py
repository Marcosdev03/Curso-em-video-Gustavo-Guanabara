from random import randint
from time import sleep
from operator import itemgetter

jogo = {'jogador 1': randint(1,6),
        'jogador 2': randint(1,6),
        'jogador 3': randint(1,6),
        'jogador 4': randint(1,6)}
raking = list()
for k, c in jogo.items():
    print(f'O {k} tirou no dado {c}')
    sleep(1)
print('-='*15)
raking = sorted(jogo.items(),key= itemgetter(1), reverse=True)
for i , v in enumerate(raking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}.')
    sleep(1)