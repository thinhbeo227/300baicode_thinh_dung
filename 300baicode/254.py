def snt(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def chen(n):
    return snt(n) and snt(n + 2)

a=[]
v=[]
e=int(input())
for i in range(e):
    b=int(input())
    a.append(b)
for x in a:
    if chen(x):
        v.append(x)
if len(v)==0:
    print("-")
else:print(*v)