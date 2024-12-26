def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print('Erro! Digite um número válido.')

# Exemplo de uso
n = leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')