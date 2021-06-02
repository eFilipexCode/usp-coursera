maxSequenceLength = int(input("Digite a quantidade de numeros da sequencia: "))

soma = 0
index = 0
while index < maxSequenceLength:
    valor = int(input("Digite um valor qualquer: "))
    soma = soma + valor
    index = index + 1

print("O resultado final eh", soma)