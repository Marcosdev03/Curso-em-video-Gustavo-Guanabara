print("Bem-vindo ao Caixa Eletrônico")
valor = int(input("Qual valor você deseja sacar? R$ "))

cedulas = [50, 20, 10, 1]
quantidade_cedulas = {}

for cedula in cedulas:
    quantidade_cedulas[cedula] = valor // cedula
    valor %= cedula

print("Você receberá:")
for cedula, quantidade in quantidade_cedulas.items():
    if quantidade > 0:
        print(f"{quantidade} cédula(s) de R${cedula}")
