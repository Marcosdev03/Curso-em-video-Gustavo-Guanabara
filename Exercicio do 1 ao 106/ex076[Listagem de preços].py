listagem = ('Lápis',1.90,
            'Caderno', 14.90,
            'Borracha',2.75,
            'Caneta',2.00,
            'Corretivo',3.75)

print('=-='*10)
print('LISTAGEM DE PRODUTOS')
print('=-='*10)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')