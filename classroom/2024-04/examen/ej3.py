def isPrime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def sumValues(matriz):
    resultado = 0
    i = 0
    for fila in matriz:
        j = 0
        for numero in fila:
            if (i + j) % 2 != 0 and isPrime(numero):
                print(numero)
                resultado = resultado + numero
            j = j + 1
        i = i + 1
    return resultado

matriz = [
        [2,3,4],
        [5,6,7],
        [8,9,10]
        ]

print(sumValues(matriz))