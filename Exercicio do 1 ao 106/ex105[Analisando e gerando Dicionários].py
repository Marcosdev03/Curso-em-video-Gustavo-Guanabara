
def notas(*n, sit=False):
    dados = {}
    dados['quantidade'] = len(n)
    dados['maior'] = max(n)
    dados['menor'] = min(n)
    dados['média'] = sum(n) / len(n)
    
    if sit:
        if dados['média'] >= 7:
            dados['situação'] = 'Boa'
        elif dados['média'] >= 5:
            dados['situação'] = 'Razoável'
        else:
            dados['situação'] = 'Ruim'
    
    return dados

# Exemplo de uso
result = notas(7, 8, 6, 5, sit=True)
print(result)
