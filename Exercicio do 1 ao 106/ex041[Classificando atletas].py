from datetime import date

ano_nasc = int(input('Digite o ano de nascimento: '))
idade = date.today().year - ano_nasc
 
print(f'O atleta tem {idade} anos.')
if idade <= 14:
    print('Classificação: mirim.')
elif idade <= 19: 
    print('Classificação: Junior.')
elif idade <= 25:
    print('Classificação: Sênior')
else:
    print('Classificação: Master.')
    