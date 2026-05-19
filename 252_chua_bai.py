def cp(a):
    if a < 0:
        return False
    x = int(a**0.5)
    return x * x == a


b = int(input())

dem = 0
for i in range(b):
    c = int(input())
    if cp(c):
        dem += 1
        print(c, end=" ")

if dem == 0:
    print("-")

# tiep tuc 253 nao =))