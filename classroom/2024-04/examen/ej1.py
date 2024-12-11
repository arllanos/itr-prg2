def intersec(lista1, lista2):
    interseccion = []
    for n in lista1:
        if n in lista2 and n not in interseccion:
            interseccion.append(n)
    return interseccion


print(intersec([1,2,3,4,5,6],[6,7,2,9]))