def ToDecimal(num):
    resultado = 0
    posiciones = range(len(num))
    exponentes = posiciones[::-1]

    for p in posiciones:
        digito = int(num[p])
        r = digito * (2 ** exponentes[p])
        resultado += r

    return resultado

print(ToDecimal("1101"))
