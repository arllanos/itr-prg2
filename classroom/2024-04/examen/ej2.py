def PedirDatos():
    c = input("ingresar cantidad de sublistas: ")
    c = int(c)
    sublistas =  []
    for _ in range(c):
        elemento = []
        e = 0
        while e != -1:
            e = input("ingrese elementos de la sublista (-1 para finalizar): ")
            e = int(e)
            if e != -1:
                elemento.append(e)
            else:
                print(f"sublista terminada: {elemento}")
                break
        sublistas.append(elemento)
    return sublistas


def UniqueValues(sublistas):
    anotador = {}

    for s in sublistas:
        print(f"{s}")
        for e in s:
            if e in anotador:
                anotador[e] += 1 
            else:
                anotador[e] = 1

    unicos = []
    for k in anotador:
        if anotador[k] == 1:
            unicos.append(k)
    return unicos

def CommonValues(lista_de_listas):
    if not lista_de_listas:
        return []
    
    # Tomamos la primera sublista como referencia
    elementos_comunes = []
    for elemento in lista_de_listas[0]:
        print(f"lista_de_listas[0]: {lista_de_listas[0]} / elemento {elemento}")
        es_comun = True
        for sublista in lista_de_listas[1:]:
            print(f"sublista: {sublista}")
            if elemento not in sublista:
                es_comun = False
                break
        if es_comun and elemento not in elementos_comunes:
            elementos_comunes.append(elemento)
    
    return elementos_comunes


# sublistas = [[1,2,3], [2,3,4], [3,4,5]]
# sublistas = [[1,2,3], [3,4,5], [3,6,7]]
sublistas = PedirDatos()

# u = UniqueValues(sublistas)
# print(u)

c = CommonValues(sublistas)
print(c)