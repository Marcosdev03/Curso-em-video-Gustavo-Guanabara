soma = 0
cont = 0
for num in range(1, 501, 2):
   if num % 3 == 0:
       cont = cont + 1
       soma += num
       
print(f'O valor da soma de todo os {cont} valores são {soma}.')       