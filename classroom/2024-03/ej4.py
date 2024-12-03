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
    #primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307]
    factores = []

    for i in primos:
        while num % i == 0:
            factores.append(i)
            num = num / i
    return factores

fp = PrimeFactors(60)
print(fp)
# CHECK
resultado = 1
for n in fp:
    resultado = resultado * n
print(resultado)
    