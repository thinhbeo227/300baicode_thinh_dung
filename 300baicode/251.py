def uia(a):
    if 2>a:
        return False
    for i in range(2, int(a**0.5) + 1): #
        if a%i==0:
            return False
    return True
a=[]
b=int(input())

for i in range(b):
    c=int(input())
    a.append(c)
dem=0
for i in range(len(a)):
    if uia(a[i])==True:
        print(a[i])
        dem=+1
if dem==0:print("-")


