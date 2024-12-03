from ej4 import PrimeFactors

def lluvia(num):
    prime_factors = PrimeFactors(num)
    # print(prime_factors)

    resultado = ""
    for f in prime_factors:
        if f == 3:
            resultado = f"{resultado}Pling"
        elif f == 5:
            resultado = f"{resultado}Plang"
        elif f == 7:
            resultado = f"{resultado}Plong"

    if resultado == "":
        resultado = str(num)
    return resultado

print(lluvia(34))