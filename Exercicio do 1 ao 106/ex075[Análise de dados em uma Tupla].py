num = ((int(input('Digite um número:'))),
       (int(input('Digite um número:'))),
       (int(input('Digite um número:'))),
       (int(input('Digite um número:')))
 )
print(f'Você digitou os valores {num}')
print(f'O nove apareceu {num.count(9)} vezes.')
if 3 in num:
    print(f'O valor 3 foi digitado na posição {num.index(3)+1}ª.')
else:
    print('O valor 3 não foi digitado.')
print('Os valores pares digitados foram ',end='')
for n in num:
    if n % 2 == 0:
     print(n, end=' ')
print()
