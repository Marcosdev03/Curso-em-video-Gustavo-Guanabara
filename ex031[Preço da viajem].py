km = float(input('Digite a distância percorrida em Km:'))
if km <= 200:
    preco_passagem = 0.50 * km
else: 
    preco_passagem = 0.45 * km 
print('O preço da passagem é R$ {:.2f}'.format(preco_passagem))
