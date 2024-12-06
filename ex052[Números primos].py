# Entrada de dados
num = int(input("Digite um número inteiro: "))

# Variável para contar divisores
divisores = 0

# Verificando se o número é primo
for i in range(1, num + 1):
    if num % i == 0:
        divisores += 1

# Exibindo o resultado
if divisores == 2:
    print(f"O número {num} é primo.")
else:
    print(f"O número {num} não é primo.")
