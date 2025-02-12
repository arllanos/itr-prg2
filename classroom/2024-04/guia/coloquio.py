def cantidadMonedas(num):
    monedas = [500, 100, 25, 10, 5, 1]
    resultado = 0
    for moneda in monedas:
        resultado = resultado + num // moneda
        num = num % moneda
    return resultado


print(cantidadMonedas(468))