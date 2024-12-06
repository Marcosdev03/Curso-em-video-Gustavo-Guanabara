# Inicializar variáveis
soma = 0
contador = 0
continuar = 'S'
maior = None
menor = None

while continuar in 'Ss':
    numero = int(input("Digite um número: "))
    soma += numero
    contador += 1
    
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero
    
    continuar = input("Quer continuar? [S/N] ").strip().upper()

# Calcular a média
media = soma / contador

# Mostrar resultados
print(f"Você digitou {contador} números.")
print(f"A média dos valores digitados é {media}.")
print(f"O maior valor digitado foi {maior}.")
print(f"O menor valor digitado foi {menor}.")
