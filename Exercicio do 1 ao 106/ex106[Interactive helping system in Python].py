from termcolor import cprint

def ajuda(comando):
    cprint(f'Consultando o comando: {comando}', 'yellow')
    help(comando)

while True:
    cprint('Digite um comando para ver o manual (ou FIM para sair):', 'blue')
    comando = input('Comando: ').strip()

    if comando.lower() == 'fim':
        cprint('Saindo do sistema...', 'red')
        break
    else:
        ajuda(comando)
