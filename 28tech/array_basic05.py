a=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(a):
    if b[i]%2==0 and i%2==0:
        c.append(b[i])
if len(c)==0:
    print("NONE")
else:
    print(*c)