
arreglo2 = range(0, 100)


print("imprimiento usando arreglo2")
for elemento in arreglo2:
    print(elemento)

# armar una variable con los numeros pares de arreglo2
# usando list comprehensions
arreglo3 = [x for x in arreglo2 if x % 2 == 0]
print("imprimiento usando arreglo3: ", arreglo3)

# armar una varaible con los numeros pares de arreglo2
# forma tradicional
resultado = []
for x in arreglo2:
    if x % 2 == 0:
        resultado.append(x)
print("imprimiento arreglo2.......: ", resultado)