# Tupla com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol (exemplo)
times = ('Atlético Mineiro', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Corinthians', 
         'Bragantino', 'Fluminense', 'América Mineiro', 'Atlético Goianiense', 
         'Santos', 'Ceará', 'Internacional', 'São Paulo', 'Athletico-PR', 
         'Cuiabá', 'Juventude', 'Bahia', 'Grêmio', 'Sport Recife', 'Chapecoense')

# a) Os 5 primeiros times
print("Os 5 primeiros times são:", times[:5])

# b) Os últimos 4 colocados
print("Os últimos 4 colocados são:", times[-4:])

# c) Times em ordem alfabética
print("Times em ordem alfabética:", sorted(times))

# d) Em que posição está o time da Chapecoense
posicao_chapecoense = times.index('Chapecoense') + 1
print("O time da Chapecoense está na posição:", posicao_chapecoense)
