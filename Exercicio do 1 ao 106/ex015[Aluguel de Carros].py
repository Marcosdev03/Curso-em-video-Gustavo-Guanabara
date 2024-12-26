km_percorridos = float(input("Digite a quantidade de Km percorridos: "))
dias_alugados = int(
    input("Digite a quantidade de dias pelos quais o carro foi alugado: "))

preco_total = (dias_alugados * 60) + (km_percorridos * 0.15)

print("O preço total a pagar é R${:.2f}".format(preco_total))
