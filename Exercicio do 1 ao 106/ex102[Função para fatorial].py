def fatorial(num, show=False):
    """
    Calcula o fatorial de um número.
    
    :param num: Número a calcular o fatorial.
    :param show: (opcional) Mostrar ou não o processo de cálculo.
    :return: O valor do fatorial do número.
    """
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show:
            print(i, end=' x ' if i > 1 else ' = ')
    return f


# Testando a função
n = int(input('Digite um número para calcular o fatorial: '))
mostrar = input('Deseja mostrar o cálculo? (s/n): ').strip().lower() == 's'
print(fatorial(n, show=mostrar))
