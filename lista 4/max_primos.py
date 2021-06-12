def isPrime(number):
    index = 1
    numeroNaoPrimo = False

    while index < number and not numeroNaoPrimo:
        if number % index == 0 and index != 1:
            numeroNaoPrimo = True
        index+= 1

    return not numeroNaoPrimo

def maior_primo(n):
    i = 0
    maiorPrimo = 0
    while i <= n:
        if isPrime(i):
            maiorPrimo = i
        i += 1
    return maiorPrimo