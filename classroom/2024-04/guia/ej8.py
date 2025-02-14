def mixDict(d1, d2):
    resultado = {}
    for k in d1:
        if k in d2:
            resultado[k] = d1[k] + d2[k]
        else:
            resultado[k] = d1[k]
    for k in d2:
        if k not in resultado:
            resultado[k] = d2[k]
    return resultado



r = mixDict(
    {'a':1, 'b':2, 'c':3},
    {'b':3, 'c':4, 'd':5}
    )

print(r)