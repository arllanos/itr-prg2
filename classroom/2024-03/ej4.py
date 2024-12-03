import math

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def ObtenerPrimosHasta(n):
    hasta = int(math.sqrt(n))

    factores = []
    for i in (range(2, hasta)):
        if isPrime(i):
            factores.append(i)
    return factores

def PrimeFactors(num):
    primos = ObtenerPrimosHasta(num)
    # if num > 1:
    factores = []
    for i in primos:
        while num % i == 0:
            factores.append(i)
            num = num / i
    return factores

fp = PrimeFactors(60)

print(fp)

resultado = 1
for n in fp:
    resultado = resultado * n
print(resultado)
    
