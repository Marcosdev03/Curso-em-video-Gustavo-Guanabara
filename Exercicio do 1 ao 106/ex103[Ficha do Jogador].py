def ficha(nome="<DESCONHECIDO>", gols=0):
    """
    Exibe a ficha do jogador com nome e número de gols.
    """
    # Verifica se os parâmetros são válidos e ajusta, se necessário.
    if not nome.strip():
        nome = "<DESCONHECIDO>"
    if not str(gols).isdigit():
        gols = 0

    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'

# Programa principal
nome = input("Digite o nome do jogador: ").strip()
gols = input(f"Quantos gols {nome if nome else 'o jogador'} fez? ").strip()

if gols.isdigit():
    gols = int(gols)
else:
    gols = 0

print(ficha(nome, gols))
