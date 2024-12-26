n1 = float(input('Digite a primeira nota do aluno :'))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2

print(f'Tirando {n1} e {n2} a sua media será {media:.1f}')

if media >= 7:
    print('Parabéns, você foi aprovado!')
elif media >= 5.0:
    print('PUXA,que pena você ficou de recuperação.')
else:
    print('PUXA! Que pena você foi reprovado.')