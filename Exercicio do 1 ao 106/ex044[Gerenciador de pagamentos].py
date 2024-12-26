while True: 
 print('='*10,'Lojas MARCOSDEV03','='*10)
 preco = float(input('Digite o valor das compras: R$'))
 avista_dinheiro = preco - (preco * 10 / 100)
 avista_cartao = preco - (preco *5 /100)
 duas_vezes = preco / 2
 total_juros = preco *20 / 100

 opcao = (input('''FORMAS DE PAGAMENTO
 [1] à vista dinheiro/cheque
 [2] à vista cartão
 [3] 2x no cartão s/juros
 [4] 3x no cartão c/juros
 ESCOLHA UMA DAS OPÇÕES:'''))
 
 if opcao == ('1'):
     print(f'A compra à vista com 10% de desconto vai ficar {avista_dinheiro:.2f} R$.')

 elif opcao == ('2'):
     print(f'A compra à vista no cartão com 5% de desconto vai ficar {avista_cartao:.2f} R$. ')

 elif opcao == ('3'):
     print(F'Sua compra dividida em duas vezes de {duas_vezes:.2f}R$ sem juros')

 elif opcao == ('4'):
   parcelas = int(input('DIGITE A QUANTIDADE DE PARCELAS:'))
   valor_parcelado = preco / parcelas
   total_compra_juros = total_juros + preco
   print(f'Sua compra parcelada em {parcelas}x de R${valor_parcelado:.2f} com juros')
   print(f'Sua compra de R${preco:.2f} vai custar {total_compra_juros:.2f} ')
   
   print('Obrigado pela compra,volte sempre!') 
   break
 else:
    print('Opção inválida,digite uma opção válida de 1 a 4 e reinicie o processo.')
    continue