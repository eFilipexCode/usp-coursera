import math
a = int(input("Digite o coeficiente quadrático (A): "))
b = int(input("Digite o coeficiente linear (B): "))
c = int(input("Digite o termo independente (C): "))

def calcularDelta(a, b, c): return b ** 2 - 4 * a * c
def calcularRaizQuadratica(b, delta, a, operation):
    if (operation == '+'):
        return (-b + math.sqrt(delta)) / (2 * a)
    else:
        return (-b - math.sqrt(delta)) / (2 * a)

delta = calcularDelta(a, b, c)
if delta < 0:
    print("esta equação não possui raízes reais")
else: 
    raizI = calcularRaizQuadratica(-b, delta, a, '+')
    if delta == 0:
        print("a raiz desta equação é", raizI)
    else: 
        raizII = calcularRaizQuadratica(-b, delta, a, '-')
        if raizI < raizII:
            print("as raízes da equação são", raizI, "e", raizII)
        else:
            print("as raízes da equação são", raizII, "e", raizI)