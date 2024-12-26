from tarfile import TruncatedHeaderError


def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if not formato else moeda(res)


def diminuir(preco=0,taxa=0,formato=False):
    res = preco - (preco * taxa / 100)
    return res if not formato else moeda(res)
    
def dobro(preco=0,formato=False):
    res = preco * 2
    return res if not formato else moeda(res)


def metade(preco=0,formato=False):
    res = preco / 2
    return res if not formato else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(preco=0,aumentar_taxa=10,reduzir_taxa=5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco,True)}')
    print(f'{aumentar_taxa}% de aumento: \t{aumentar(preco, aumentar_taxa, True)}')
    print(f'{reduzir_taxa}% de redução: \t{diminuir(preco, reduzir_taxa, True)}')
    print('-' * 30)



    
    
    