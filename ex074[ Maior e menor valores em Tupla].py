from random import randint

num_sorteados =  (randint(1, 9),
                 randint(1, 9),
                 randint(1, 9),
                 randint(1, 9),
                 randint(1, 9))
print(f'Os números sorteados foram {num_sorteados}')
print(f'O maior número sorteado foi o {max(num_sorteados)}.')
print(f'O menor número sorteado foi o {min(num_sorteados)}.')