def ToDecimal(num):
    resultado = 0
    posiciones = list(range(len(num)))
    exponentes = posiciones[::-1]

    for i in exponentes:
        r = int(num[i]) * (2**exponentes[i])
        resultado = resultado + r
    return resultado

print(ToDecimal("1101"))
