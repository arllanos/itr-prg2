# (4 * (10**1)) + ( 2*(10**0))

# input
num_decimal = 101010
base = 2

# algoritmo
i = len(str(num_decimal))-1 # 5
resultado = 0
for d in str(num_decimal):
    termino = (int(d) * (base**i))
    print(f"{d} * {base}^{i} = {termino}")
    i = i - 1
    resultado = resultado + termino

print(resultado)


# (1 * 2**5) + (0 * 2**4) + (1 * 2**3) + (0 * 2**2) + (1 * 2**1) + (0 * 2**0)