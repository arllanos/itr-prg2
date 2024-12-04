def collatz(num):
    print(num)
    # condicion de corte
    if num == 1:
        return num
    
    if num % 2 == 0:
        collatz(num/2)
    else:
        collatz((3*num) + 1)

r = collatz(22)
print(r)