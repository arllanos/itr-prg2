def MultMatrix(matriz1, matriz2):
    resultado = []
    for f in range(len(matriz1)):
        res_fila = []
        for c in range(len(matriz1[0])):
            res = matriz1[f][c] + matriz2[f][c]
            res_fila.append(res)
        resultado.append(res_fila)
    return resultado


r = MultMatrix([[1, 2], [3, 4], [5, 6]],[[7, 8, 9], [10, 11, 12]])
print(r)