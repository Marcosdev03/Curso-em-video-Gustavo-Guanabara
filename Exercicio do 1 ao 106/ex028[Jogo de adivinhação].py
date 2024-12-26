import random
numero_computador = random.randint(0 , 5)
num_user = int(input('Adivinhe o número entre 0 é 5:'))
if numero_computador == num_user:
    print('Parabéns você adivinhou o número era:',numero_computador)
else:
    print('Você errou, o numero era',numero_computador)