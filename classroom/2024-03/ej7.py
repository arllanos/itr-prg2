"""
Implementar una función que calcule la codificación y de decodificación utilizando el método de codificación de longitud de carrera.
Ayuda: La codificación de longitud de carrera (RLE) es una forma sencilla de compresión de
datos, en la que las que los elementos de datos consecutivos se sustituyen por un solo valor de datos y un recuento.
Ejemplos:
Por ejemplo, podemos representar los 53 caracteres originales con sólo 13
WWWWWWWWWWWWBWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
=>
WWWWWWWWWWWW                                    12 W
B                                               1  B
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW        40 W
            c       cont       c_anterior   resultado
-----------------------------------------------------
Nueva letra W       1           ""           f"{resultado}{c_anterior}{cont}" => ""
Misma letra W       c+1         "W"          ""

Nueva letra A       1           "W"          f"{resultado}{c_anterior}{cont}" => "W2"
Misma letra A       c+1         "A"          --
Misma letra A       c+1         "A"          --

Nueva letra C       1           "A"          f"{resultado}{c_anterior}{cont}" => "W2A3"
Misma letra C       c+1         "C"          
--                                           f"{resultado}{c_anterior}{cont}" 
"""

def rle(cadena):
    resultado, c_anterior, cont = "", "", 0

    for c in cadena:
        if c != c_anterior:  # nueva letra o comienzo de la cadena
            resultado = f"{resultado}{c_anterior}{cont}" if cont > 0 else ""
            cont = 1
        else:  # misma letra
            cont = cont + 1
        c_anterior = c

    resultado = f"{resultado}{c_anterior}{cont}" if cont > 0 else ""
    return resultado



c = rle("WWAAACCW")
print(c)


        
