number = int(input("Digite um numero: "))

index = 0
produtoFinal = 1

while index < number:
    produtoFinal = produtoFinal * (index + 1)
    index = index + 1

print(produtoFinal)