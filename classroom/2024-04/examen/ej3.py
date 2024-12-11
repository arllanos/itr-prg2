def isPrime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def sumValues(matriz):
    resultado = 0
    # for x, fila in enumerate(matriz):
    for fila in matriz:
        # for y, numero in enumerate(fila):
        for numero in fila:
            if (numero) % 2 != 0 and isPrime(numero):
                resultado = resultado + numero
    return resultado

matriz = [
        [2,3,4],
        [5,6,7],
        [8,9,10]
        ]

print(sumValues(matriz))