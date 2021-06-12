def maximoDois(a, b):
    if a > b:
        return a
    return b;

def maximo(a, b, c):
    maiorAB = maximoDois(a, b)
    maior = maximoDois(maiorAB, c)
    return maior