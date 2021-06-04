def calcFatorial(number):
    index = 0
    produtoFinal = 1

    while index < number:
        produtoFinal = produtoFinal * (index + 1)
        index = index + 1
    return produtoFinal

number = int(input("Digite N: "))
k = int(input("Digite K: "))

binomial = calcFatorial(number) / (calcFatorial(k) * (calcFatorial(number - k)))

print(binomial)