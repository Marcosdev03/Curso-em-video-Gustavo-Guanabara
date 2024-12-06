# Entrada de dados
a1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))

# Exibindo os 10 primeiros termos
print("Os 10 primeiros termos da PA são:")
for i in range(10):
    termo = a1 + i * r
    print(termo, end=' ')
