import os

while True:
 
  
  num = int(input('Digite um número para ver sua tabuada de:'))

  for c in range(1, 11):
     print(f'A tabuada de {num} x {c} = {num * c}')
     print('-'*25)
    
 
  input('Aperte ENTER para continuar:' )
  os.system('clear')
  continue
 