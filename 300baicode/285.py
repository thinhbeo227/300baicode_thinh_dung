n=int(input())
a=[]
for i in range(n):
    c=input()
    diem=float(c.split()[-1])
    ten=c.split()[:-1]
    ten=" ".join(ten)
    a.append((ten,diem))
a.sort(key=lambda x:x[1])
for i in a:
    print(*i)