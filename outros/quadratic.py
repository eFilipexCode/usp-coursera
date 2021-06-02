import math

a = int(input("Digite o coeficiente quadrático (A): "))
b = int(input("Digite o coeficiente linear (B): "))
c = int (input("Digite o termo independente (C): "))

delta = b ** 2 - 4 * a * c

if delta < 0:
    print("Equação não tem números reais!")
else: 
    print("Delta =", delta)
    if delta > 0:
        raizI = (-b + math.sqrt(delta)) / (2 * a)
        raizII = (-b - math.sqrt(delta)) / (2 * a)
        print("S = {", raizI, ",",raizII, "}")
    else: 
        raizI = (-b + math.sqrt(delta)) / (2 * a)
        print("S = {", raizI, "}")