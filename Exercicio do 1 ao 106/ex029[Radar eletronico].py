velocidade = float(input('Digite a velocidade do veiculo:'))
velocidade_maxima = 80
valor_da_multa = (velocidade - velocidade_maxima) * 7

if velocidade >= velocidade_maxima:
    print('Você foi multado em {:.2f} R$'.format(valor_da_multa))
else:
    print('Você está dentro da velocidade maxima permite.\nBoa viajem!')