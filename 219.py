def cp(a):
    if a < 0:
        return False
    b = int(a ** (1 / 2))
    return b * b == a


dong, cot = map(int, input().split())
a = []
d = 0
for i in range(dong):
    n = list(map(int, input().split()))
    a.append(n)
for row in a:
    for i in row:
        if cp(i) == True:
            print(i)
            d = d + 1
if d == 0:
    print(-1)
