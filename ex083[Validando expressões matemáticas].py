expressao = input('Digite uma expressão: ')
pilha = []

for char in expressao:
    if char == '(':
        pilha.append('(')  # Adiciona à pilha quando encontra um parêntese aberto
    elif char == ')':
        if len(pilha) > 0:
            pilha.pop()  # Remove o último parêntese aberto se houver
        else:
            pilha.append(')')  # Adiciona se encontrar um parêntese fechado sem par aberto

if len(pilha) == 0:
    print('A expressão está válida!')
else:
    print('A expressão está inválida!')
