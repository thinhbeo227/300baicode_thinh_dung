from math import gcd

a,b=map(int,input().split())
x =gcd(a,b)
a=a//x
b=b//x
print(f"{a}/{b}")
