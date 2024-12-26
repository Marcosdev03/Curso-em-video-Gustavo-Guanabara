from time import sleep


def contador (i, f, p):
    print(f'Contagem de {i} até {f} em {p}.')
    
    if i <f:
        cont = 1
        while cont <= f:
            print(f'{cont}', end='')
            sleep(0.5)
            cont += p
            print('FIM')
            

#programa principal
contador(1, 10, 1)