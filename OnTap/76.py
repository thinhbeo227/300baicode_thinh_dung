m,n=map(int,input().split())
d1=0
d2=0
for i in range(m,n+1):
    if i%2==0:
        d1=d1+i
        d2=d2+1
if d2==0:
    print(0)
else:
    print(d1//d2)