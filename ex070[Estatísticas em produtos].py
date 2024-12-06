total_gasto = 0
produtos_acima_1000 = 0
produto_mais_barato = ''
preco_mais_barato = float('inf')

while True:
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o preço do produto: "))
    
    total_gasto += preco_produto
    
    if preco_produto > 1000:
        produtos_acima_1000 += 1
        
    if preco_produto < preco_mais_barato:
        preco_mais_barato = preco_produto
        produto_mais_barato = nome_produto
    
    continuar = ''
    while continuar not in 'SN':
        continuar = input("Quer continuar? [S/N]: ").strip().upper()
    if continuar == 'N':
        break

print(f"A) Total gasto na compra: R${total_gasto:.2f}")
print(f"B) Quantos produtos custam mais de R$1000: {produtos_acima_1000}")
print(f"C) Nome do produto mais barato: {produto_mais_barato}")
