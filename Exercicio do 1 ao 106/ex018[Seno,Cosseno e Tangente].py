from math import sin, cos, tan, radians

angulo = float(input("Digite o valor do ângulo: "))
angulo_rad = radians(angulo)

seno = sin(angulo_rad)
cosseno = cos(angulo_rad)
tangente = tan(angulo_rad)

print("Para o ângulo de {}°:".format(angulo))
print("Seno: {:.2f}".format(seno))
print("Cosseno: {:.2f}".format(cosseno))
print("Tangente: {:.2f}".format(tangente))
