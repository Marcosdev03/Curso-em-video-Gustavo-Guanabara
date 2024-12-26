# Solicitar ao usuário que insira o primeiro termo e a razão da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Inicializar variáveis
termo = primeiro_termo
contador = 1

# Mostrar os 10 primeiros termos da PA
print("Os 10 primeiros termos da PA são:")
while contador <= 10:
    print(f"{termo}", end=" → ")
    termo += razao
    contador += 1
print("FIM")
