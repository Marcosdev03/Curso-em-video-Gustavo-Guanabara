nome = str(input('Digite seu nome:'))
quantidade = len(nome.replace(' ','' ))
primeiro_nome = nome.split()[0]
pm = len(primeiro_nome)
print('O nome com todas letras minusculas é ',nome)
print('O nome com todas letras maiusculas é ',nome.upper())
print(('Quanta letras tem o nome sem considerar os espaçoes'),quantidade)
print('O primeiro nome tem {} letras'.format(pm))