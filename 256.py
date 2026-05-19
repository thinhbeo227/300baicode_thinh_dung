def abc(n:int):
    n=str(n)
    tong=0
    for i in n:
        tong=tong+int(i)
    return tong
a=[]
u=int(input())
for i in range(u):
    c=abs(int(input()))
    a.append(abc(c))
print(*a)