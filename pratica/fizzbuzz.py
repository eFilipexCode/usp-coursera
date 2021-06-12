def fizzbuzz(n):
    multiploDeTres = n % 3 == 0
    multiploDeCinco = n % 5 == 0

    if (multiploDeTres and multiploDeCinco):
        return 'FizzBuzz'
    if (multiploDeTres):
        return 'Fizz'
    if (multiploDeCinco):
        return 'Buzz'
    
    return n