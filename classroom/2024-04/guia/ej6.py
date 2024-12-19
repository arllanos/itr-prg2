def invert(d):
    resultado = {}
    for k in d:
        if d[k] not in resultado:
            resultado[d[k]] = [k]
        else:
            resultado[d[k]] = resultado[d[k]] + [k]
    return resultado

print(invert({'a': 1, 'b': 2, 'c': 1, 'd': 3}))
