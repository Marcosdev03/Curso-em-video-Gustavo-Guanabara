salario = float(input('Qual é o salario do funcionario? :'))
novo = salario + (salario * 4.5/100)
print(
    'O novo salario do funcionario com aumento de 4,5% é {:.2f} R$.'.format(novo))
