a,b,c=map(int,input().split())

cv = a + b + c
p = cv / 2
'''
nua chu vi la cv / 2
the chua hieu cai gi =))
đa
'''
from math import sqrt
s = sqrt(p * (p - a)*(p-b)*(p-c))
print(cv)
print(f"{s:.3f}")