num_por_extenso = ('zero','um','dois','tres','quatro','cinco','seis',
'sete','oito','nove','dez',
'onze','doze','treze','quatroze','quinze',
'dezesseis','dezessete','dezoito','dezenove','vinte'
)

while True:
    num = int(input('Digite um número entre 1 e 20: '))
    if 0 <= num <= 20:
        break
    print('Digite um numero válido, tente novamente.')
print(f'Você digitou o número {num_por_extenso[num]}.')

    