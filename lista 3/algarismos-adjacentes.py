number = int(input("Digite um numero: "))

anterior = number - 1
valorAtual = 0
qtdDeAlgarismos = len(str(number))

adjacentesIguais = False
i = 0
while i < qtdDeAlgarismos and not adjacentesIguais:
    valorAtual = number % 10
    if valorAtual == anterior:
        adjacentesIguais = True
    else:
        i += 1
        anterior = valorAtual
        number = number // 10

if adjacentesIguais:
    print("sim")
else:
    print("não")