def nguyen(a):
    if a<2:
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True
        
        
a=int(input())
b=list(map(int,input().split()))
d=0
t=0
for i in range(a):
    if nguyen(b[i]):
        d=d+1
        t=t+b[i]
print(f"{t/d:.3f}")