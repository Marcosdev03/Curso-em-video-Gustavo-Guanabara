total_maior_18 = 0
total_homens = 0
total_mulheres_menos_20 = 0

while True:
    idade = int(input("Digite a idade: "))
    sexo = ''
    while sexo not in 'MF':
        sexo = input("Digite o sexo [M/F]: ").strip().upper()

    if idade > 18:
        total_maior_18 += 1
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 20:
        total_mulheres_menos_20 += 1

    continuar = ''
    while continuar not in 'SN':
        continuar = input("Quer continuar? [S/N]: ").strip().upper()
    if continuar == 'N':
        break

print(f"A) Total de pessoas com mais de 18 anos: {total_maior_18}")
print(f"B) Total de homens cadastrados: {total_homens}")
print(f"C) Total de mulheres com menos de 20 anos: {total_mulheres_menos_20}")
