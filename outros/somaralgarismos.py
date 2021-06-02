number = int(input("Digite um numero inteiro: "))
numberLength = len(str(number))

index = 0
somaFinal = 0

while index < numberLength:
    somaFinal += number % 10
    number = number // 10
    index += 1

print(somaFinal)