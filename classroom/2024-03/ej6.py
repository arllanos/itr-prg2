# (4 * (10**1)) + ( 2*(10**0))

# input
numero = 101010
base = 2

# algoritmo
exponente = len(str(numero))-1 # 5
resultado = 0
for d in str(numero):
    termino = int(d) * (base**exponente)
    print(f"{d} * {base}^{exponente} = {termino}")
    exponente = exponente - 1
    resultado = resultado + termino

print(resultado)


# (1 * 2**5) + (0 * 2**4) + (1 * 2**3) + (0 * 2**2) + (1 * 2**1) + (0 * 2**0)