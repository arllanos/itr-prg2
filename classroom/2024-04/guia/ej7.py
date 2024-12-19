def averageKeys(d):
    lista = list(d)  # ['a', 'b' , 'c']
    promedios  = {}
    
    for k in lista:
        resultado = 0
        fila = d[k]
        for e in fila:
            resultado = resultado + e
            promedio = resultado / len(lista)
            promedios[k] = promedio
    return promedios
        

d = {'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}
r = averageKeys(d)
print(r)