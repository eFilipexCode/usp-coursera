import math

a = int(input("Digite o coeficiente quadrático (A): "))
b = int(input("Digite o coeficiente linear (B): "))
c = int(input("Digite o termo independente (C): "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("esta equação não possui raízes reais")
else: 
    raizI = (-b + math.sqrt(delta)) / (2 * a)
    if delta == 0:
        print("a raiz desta equação é", raizI)
    else: 
        raizII = (-b - math.sqrt(delta)) / (2 * a)
        if raizI < raizII:
            print("as raízes da equação são", raizI, "e", raizII)
        else:
            print("as raízes da equação são", raizII, "e", raizI)