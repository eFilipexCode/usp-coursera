import math

pontoA_x = float(input("Digite a coordenada X do ponto A: "))
pontoA_y = float(input("Digite a coordenada X do ponto A: "))
pontoB_x = float(input("Digite a coordenada X do ponto B: "))
pontoB_y = float(input("Digite a coordenada X do ponto B: "))

distancia = math.sqrt(math.pow(pontoB_x - pontoA_x, 2) + math.pow(pontoB_y - pontoA_y, 2))

if distancia >= 10:
    print("longe")
else:
    print("perto")