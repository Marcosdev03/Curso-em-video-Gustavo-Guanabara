def area(c,l): 
  area = comprimento * largura
  print(f'O terreno com o comprimento de {comprimento} m² por {largura} de largura tem a área de {area:.2f} m².')

print('-='*10)
print('CONTROLE DE TERRENO')
print('-='*10)
comprimento = float(input('Digite o comprimento: '))
largura =float(input('Digite a largura: '))
area(comprimento, largura)