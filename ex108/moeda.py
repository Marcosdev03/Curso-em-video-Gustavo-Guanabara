def aumentar(preco=0, taxa=0, formato=False):
    res = preco + (preco * taxa / 100)
    return res if formato is False else res(moeda)

def diminuir(preco=0,taxa=0,formato=0):
    res = preco - (preco * taxa / 100)
    return res if formato is False else res(moeda)
    
def dobro(preco=0,formato=0):
    res = preco * 2
    return res if formato is False else res(moeda)


def metade(preco=0):
    res = preco / 2
    return res


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


    
    
    