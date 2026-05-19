def tg(a,b,c):
    if a<=0 or b <=0 or c<=0:
        return False
    if a+b>c and a+c>b and b+c>a:
        return True
    return False
def cv(a,b,c):
    return (a+b+c)
from math import sqrt
def dt(a,b,c):
    p=cv(a,b,c)/2
    return sqrt(p*(p-a)*(p-b)*(p-c))
x,y,z=map(int,input().split())
if tg(x,y,z):
    print("Day la 3 canh cua mot tam giac")
    print(f"{cv(x,y,z):.2f}",end=" ")
    print(f"{dt(x,y,z):.1f}")
else:
    print("Day khong phai la 3 canh cua mot tam giac")