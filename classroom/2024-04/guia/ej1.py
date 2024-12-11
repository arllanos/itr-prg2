def partList(lista, k):
    menores_k = []
    mayores_k = []

    for num in lista:
        if num < k:
            menores_k.append(num)
        else:
            mayores_k.append(num)
    return menores_k + mayores_k

r = partList([4, 3, 2, 1, 5, 6] ,4)
print(r)