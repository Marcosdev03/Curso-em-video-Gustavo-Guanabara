while True:
 from random import randint 
 import os
 from time import sleep
 

 print('='*10,'JOGO PEDRA, PAPEL, TESOURA','='*10)

 itens = ('pedra', 'papel', 'tesoura')
 computador = randint(0, 2)
 jogador = print('''ESCOLHA UMA OPÇÃO:
[0] PEDRA
[1] PAPEL
[2] TESOURA
===========''')
 jogador = int(input('Qual é sua jogada:'))
 print('PEDRA')
 sleep(1)
 print('PAPEL')
 sleep(2)
 print('TESOURA...')
 sleep(1)
 print('-='*11)
 print(f'Computador jogou {itens[computador]}')
 print(f'Jogador jogou {itens[jogador]}')
 print('-='*11)
 if computador == 0:
     if jogador == 0:
      print('EMPATOU!')
     elif jogador == 1:
       print('PARABÉNS,VOCÊ VENCEU')
     elif jogador == 2:
        print('QUE PENA, VOCÊ PERDE TENTE NOVAMENTE!')
     else:
         print('OPÇÂO INVÁLIDA, TENTE NOVAMENTE')
    
 elif computador == 1:
     if jogador == 0:
         print('QUE PENA, VOCÊ PERDEU TENTE NOVAMENTE')
     elif jogador == 1:
         print('EMPATOU!')
     elif jogador == 2:
         print('QUE PENA, VOCÊ PERDEU TENTE NOVAMENTE!')
     else:
         print('OPÇÃO INVÁLIDA TENTE NOVAMENTE.')
        
 elif computador == 2:
     if jogador == 0:
      print('PARABÉNS, VOCÊ VENCEU!')
     elif jogador == 1:
      print('QUE PENA, VOCÊ PERDEU TENTE NOVAMENTE!')
     elif jogador == 2:
       print('EMPATOU!')
       
    
 input("Pressione Enter para continuar Jogando...")  # Aguarda o jogador apertar Enter
 os.system('clear')
 continue
     
             