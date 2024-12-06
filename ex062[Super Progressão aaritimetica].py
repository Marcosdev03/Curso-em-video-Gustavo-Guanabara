# Solicitar ao usuário que insira o primeiro termo e a razão da PA
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

# Inicializar variáveis
termo = primeiro_termo
contador = 1
total_termos = 0
mais_termos = 10  # Iniciar com 10 termos

# Mostrar os termos da PA conforme solicitação do usuário
while mais_termos != 0:
    total_termos += mais_termos
    while contador <= total_termos:
        print(f"{termo}", end=" → ")
        termo += razao
        contador += 1
    print("PAUSA")
    mais_termos = int(input("Quantos termos você quer mostrar a mais? (Digite 0 para encerrar): "))

print(f"Progressão finalizada com {total_termos} termos mostrados.")
