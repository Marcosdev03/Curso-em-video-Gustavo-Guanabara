import random
computador = random.randint(1, 10)
erros = 1

palpite = int(input('''Sou seu computador...
Acabei de pensar em um número entre 1 e 10.
Será que você consegue adivinhar qual foi?
Qual é o palpite?: '''))

while palpite != computador:
    erros += 1
    if palpite > computador:
     print('Menos que isso...')
    else:
     print('Mais que isso...')
    palpite = int(input('Qual é o seu palpite: '))
    

    
print(f'Você acertou com {erros} tentativas, o número escolhido pelo computador foi {computador}.')


