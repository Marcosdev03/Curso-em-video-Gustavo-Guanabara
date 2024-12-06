from time import sleep

primeiro_valor = int(input('Digite o primeiro valor: '))
segundo_valor = int(input('Digite o segundo valor: '))

while  True:
    opcao = input('''Escolha uma das opções
 [1] Somar
 [2] Multiplicar
 [3] Maior
 [4] Novo número
 [5] Sair do programa.
 Opção: ''')
    print('=''-'*20)
    if opcao == '1':
        print(f'A soma entre {primeiro_valor} e {segundo_valor} é {(primeiro_valor + segundo_valor)}')
        print('=''-'*20)
    elif opcao == '2':
        print(f'A multiplicação entre {primeiro_valor} e {segundo_valor} é {(primeiro_valor * segundo_valor)}')
        print('=''-'*20)
    elif opcao == '3':
        maior = max(primeiro_valor,segundo_valor)
        print(f'O maior entre {primeiro_valor} e {segundo_valor} é {(maior)}')
        print('=''-'*20)
    elif opcao == '4':
       primeiro_valor = int(input('Digite o primeiro valor: '))
       segundo_valor = int(input('Digite o segundo valor: '))
    elif opcao == '5':
        print('Saindo do programa...')
        sleep(2)
        break
    else:
        print('Opção inválida tente novamente!')
        
        
        
        
        
        
        
        


 
