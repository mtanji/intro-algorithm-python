# Q11

print("======= a =======")
def bacteriasA(n):
    return bacteriasA(n-2)

print("======= b =======")
def bacteriasB(n):
    return (n - 2 + n - 1)

print("======= c =======")
def bacteriasC(n):
    return (n - 2 + n - 1)

print("======= d =======")
def bacteriasD(n):
    return ( bacteriasD(n-2) + bacteriasD(n-1) )

print("======= e =======")
def bacteriasE(n):
    if n <= 1:
        return 1
    else:
        return ( bacteriasE(n-2) + bacteriasE(n-1) )

print(bacteriasE(1))
print(bacteriasE(2))
print(bacteriasE(3))
print(bacteriasE(4))
print(bacteriasE(5))
