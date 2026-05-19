def pika(ka):
    if ka<2:
        return False
    for i in range(2,ka):
        if ka%i==0:
            return False
    return True
dong, so = map(int, input().split())
a = []
t = 0
for i in range(dong):
    n = list(map(int, input().split()))
    a.append(n)
s = 0
for row in a:
    for x in row:
        if pika(x):
            s=s+1
print(s)