# Solicitar ao usuário que insira o número de termos da sequência
N = int(input("Digite o número de termos da Sequência de Fibonacci: "))

# Inicializar os dois primeiros termos da sequência
a, b = 0, 1
contador = 0

print("Os primeiros", N, "termos da Sequência de Fibonacci são:")

# Calcular e mostrar os N primeiros termos
while contador < N:
    print(a, end=" → ")
    a, b = b, a + b
    contador += 1

print("FIM")
