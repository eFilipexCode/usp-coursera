number = int(input("Digite um número inteiro: "))

resto100= number % 100
resto10 = number % 10

print("O dígito das dezenas é", (resto100 - resto10) // 10)