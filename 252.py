def uia(a):
    if a<0:
        return False
    x = int(a**0.5)
    return x * x == a
a=[]
b=int(input())

for i in range(b):
    c=int(input())
    a.append(c)
dem=0
thanhhoa36=[]
for i in range(len(a)):
    
    if uia(a[i])==True:
        thanhhoa36.append(a[i])
        dem=+1
if dem==0:print("-")
else: print(*thanhhoa36)
