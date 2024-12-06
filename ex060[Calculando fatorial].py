# Solicitar ao usuário que insira um número
numero = int(input("Digite um número para calcular o fatorial: "))

# Inicializar a variável do fatorial
fatorial = 1

# Calcular o fatorial
for i in range(1, numero + 1):
    fatorial *= i

# Mostrar o resultado
print(f"O fatorial de {numero} é {fatorial}")
