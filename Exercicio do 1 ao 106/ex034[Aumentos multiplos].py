salario = int(input('Digite quanto o funcionario recebe: '))
if salario > 1250:
    aumento_salario = salario + salario * 10 / 100
else:
    aumento_salario = salario + salario * 15 / 100
print('O salario passou a ser {:.2f}'.format(aumento_salario))