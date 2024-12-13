def averageKeys(d):
    resultado = {}
    key = [x for x in d]
    for i in range(len(d)):
        fila = d[key[i]]
        suma = 0
        contador = 0
        for n in fila:
            suma = suma + n
            contador = contador + 1
            promedio = suma / contador
            resultado[key[i]] = promedio
    return resultado   


d = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
r = averageKeys(d)
print(r)