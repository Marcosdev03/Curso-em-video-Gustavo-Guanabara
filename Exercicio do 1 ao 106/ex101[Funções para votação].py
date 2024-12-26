from datetime import date
def voto(ano):
    idade = date.today().year - ano
    frase = 'OBRIGATORIEDADE DE VOTO'
    print('='*len(frase))
    print(frase)
    print('='*len(frase))
    if 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos de idade:[VOTO OPCIONAL!]'
    elif 18 <= idade <= 65:
        return f'Com {idade} anos de idade:[VOTO OBRIGATÓRIO!]'
    else:
        return f'Com {idade} anos de idade:[NÃO VOTA!]'
    

while True:   
    try:
        ano = int(input('Digite o ano de nascimento: '))
        print(voto(ano))
        break
    except ValueError:
        print('Digite um ano valido!')
    







