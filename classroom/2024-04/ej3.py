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
    for x in range(len(matriz)):
        # for y, numero in enumerate(fila):
        for y in range(len(matriz[0])):
            print(f"[{x}][{y}]:  {matriz[x][y]}")
            if (x+y) % 2 != 0 and isPrime(matriz[x][y]):
                resultado = resultado + matriz[x][y]
    return resultado

matriz = [
        [2,3,4],
        [5,6,7],
        [8,9,10]
        ]

print(sumValues(matriz))