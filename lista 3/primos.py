number = int(input("Digite algum numero: "))

index = 1
numeroNaoPrimo = False

while index < number and not numeroNaoPrimo:
    if number % index == 0 and index != 1:
        numeroNaoPrimo = True
    index+= 1

if numeroNaoPrimo:
    print("não primo")
else:
    print("primo") 