# Entrada de dados
valor_imovel = float(input('Digite o valor do imóvel desejado: '))
salario_comprador = float(input('Digite o salário do comprador: '))
anos_a_pagar = float(input('Digite em quantos anos deseja pagar: '))

# Calculando o número total de parcelas (meses)
parcelas = anos_a_pagar * 12

# Calculando o valor da parcela mensal
valor_da_parcela = valor_imovel / parcelas

# Calculando 30% do salário do comprador
limite_parcela = salario_comprador * 30 / 100

# Exibindo o valor da parcela mensal
print(f'O valor da parcela mensal será: R${valor_da_parcela:.2f}')

# Verificando se o valor da parcela excede 30% do salário
if valor_da_parcela > limite_parcela:
    print('Empréstimo negado! O valor da parcela excede 30% do seu salário.')
else:
    print('Empréstimo aprovado! Você pode pagar este imóvel.')












'''
valor_imovel = float(input('Digite o valor do imóvel desejado: '))
salario_comprador = float(input('Digite o salário do comprador: '))
parcelas = float(input('Digite a quantidade de parcelas: '))
valor_permitido_de_parcelas = salario_comprador * 30 / 100

if parcelas >= valor_permitido_de_parcelas:
        print('Emprestimo negado.')
else:
    print('Parabéns seu emprestimo foi autorizado pelo banco.')

'''