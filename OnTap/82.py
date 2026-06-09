import math
from math import gcd 
b,a=map(int,input().split())
x=math.gcd(b, a)
b=b//x
a=a//x
print(f"{b:.0f}/{a:.0f}")

'''
a = 15
b = 20
15/20

x = 5
15/5 = 3
20/5 = 4



x  =gcd(a, b)
a  /= x

b /= x
print(f'{a}/{b})
'''