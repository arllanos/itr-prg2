def rotateList(lista, k):
    i = 0
    resultado = [0 for x in lista]

    for e in lista:
        if (i+k) < len(lista):
            resultado[i+k] = e
        else:
            m = (i+k) - len(lista)
            resultado[m] = e
        i = i + 1
    return resultado        

r = rotateList([1, 2, 3, 4, 5],2)
print(r)