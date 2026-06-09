def uia(x):
    if x < 2: 
        return False
    for i in range(2,x):
        if x %i ==0:
            return False
    return True
h,k=map(int,input().split())
u=0
for i in range(h,k+1):
    if uia(i):
        u=u+i
print(u)        
