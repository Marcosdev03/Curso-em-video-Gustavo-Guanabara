import random

vitorias = 0

while True:
    jogador_num = int(input("Digite um número: "))
    escolha = input("Par ou Ímpar? [P/I]: ").strip().upper()
    computador_num = random.randint(0, 10)
    total = jogador_num + computador_num
    resultado = 'P' if total % 2 == 0 else 'I'

    print(f"Você jogou {jogador_num} e o computador jogou {computador_num}. Total de {total} deu {'PAR' if resultado == 'P' else 'ÍMPAR'}.")

    if resultado == escolha:
        print("Você venceu!")
        vitorias += 1
    else:
        print("Você perdeu!")
        break

print(f"Fim de jogo! Você teve {vitorias} vitórias consecutivas.")
