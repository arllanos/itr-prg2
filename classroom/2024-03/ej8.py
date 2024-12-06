def collatz(num):
    pasos = 0
    resultado = 1
    while num > 1:
        if num % 2 == 0:
            num = num / 2
            
        elif num % 2 != 0:
            num = num*3 + 1
        pasos = pasos + 1 #esto calcula la cantidad de pasos que necesitas para llegar al numero 1
        resultado = num
        print(f"Paso {pasos}:  {num}") 
    return resultado

print(f"ultimo numero: {collatz(10)}")