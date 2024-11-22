from datetime import date

ano_nac = int(input('Digite o ano do seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nac




if ano_atual - ano_nac >= 18:
    print(f'você já tem {idade} anos, você ja deveria ter se alistado')
    saldo = idade - 18
elif ano_atual - ano_nac <= 18:
    saldo = 18 - idade
    print(f'Você tem  {idade} anos ainda faltam {saldo}')