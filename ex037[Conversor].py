while True:
    numero = int(input('Digite um número: '))
    print('''Escolha uma das bases para conversão:
    [1] Converter para BINÁRIO.
    [2] Converter para OCTAL.
    [3] Converter para HEXADECIMAL.
    [4] Sair do programa.    
    ''')
    opcao = int(input('Escolha uma das opções: '))

    if opcao == 1:
        print(f'{numero} convertido para BINÁRIO será {bin(numero)[2:]}')
    elif opcao == 2:
        print(f'{numero} convertido para OCTAL será {oct(numero)[2:]}')
    elif opcao == 3:
        print(f'{numero} convertido para HEXADECIMAL será {hex(numero)[2:]}')
    elif opcao == 4:
        break
    else:
        print('Opção inválida, digite um número inteiro.')
   