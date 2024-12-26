sexo = str(input('Informe seu sexo [M/F]:')).upper().strip()
while sexo not in ['M','F']:
    sexo = str(input('Opção invalida,por informe seu sexo [M/F]:')).strip().upper()
print(f'Sexo {sexo} registrado com sucesso!')
    