"""
0000 0
0001 1
0010 2
0011 3
0100 4 
0101 5
0110 6
0111 7
1000 8
1001 9
1010 10
1011 11
1100 12
1101 13
1110 14
1111 15
"""
def ToBinary(num):
    restos = []
    cociente = num
    while int(cociente) > 0:
        resto = cociente % 2
        cociente = cociente // 2
        restos.append(resto)
    return restos[::-1]

print(ToBinary(13))
