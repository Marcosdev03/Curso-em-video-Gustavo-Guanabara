import math

num = int(input('Digite um número:'))
d = num * 2
t = num * 3
r = math.sqrt(num)
print('O dobro de {} é {}.'.format(num, d))
print('O triplo de {} é {}.'.format(num, t))
print('A raiz quadrada de {} é {:.2f}.'.format(num, r))
