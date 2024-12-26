# Tupla com várias palavras
palavras = ('banana', 'abacaxi', 'melancia', 'laranja', 'manga')

# Exibe as vogais de cada palavra
for palavra in palavras:
    vogais = [letra for letra in palavra if letra in 'aeiou']
    print(f'Na palavra "{palavra}", as vogais são: {", ".join(vogais)}')
