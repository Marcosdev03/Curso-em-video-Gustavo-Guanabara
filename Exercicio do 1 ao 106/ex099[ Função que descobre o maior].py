from time import sleep


def maior(*núm):
    cont = maior = 0
    print(f'\nAnalisando valores passados...')
    for valor in núm:
        print(f'{valor} ',end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1 
    print()
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
    
    
maior(10, 1, 5, 7, 45, 69)