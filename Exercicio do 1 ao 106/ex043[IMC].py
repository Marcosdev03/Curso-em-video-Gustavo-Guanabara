peso = float(input('Digite seu peso: (KG) '))
altura = float(input('Digite sua altura: (Mtrs) '))
imc = peso / altura** 2 

print(f'O seu peso é {peso} kg.')
print(f'A sua altura é {altura}.')
print(f'Seu indice de massa corporal é {imc:.2f}')

if imc < 18.5: 
    print('Você está abaixo do peso normal')

elif  18.5 <= imc <= 25: 
    print('Parabéns, você está no peso ideal')

elif 25 <= imc <= 30: 
    print('Você está acima do peso.')

elif 30 <= imc <= 40: 
    print('Cuidado você apresenta sinais de Obesidade')

else:
    print('ATENÇÃO! você está em  Obesidade Mórbida')
    