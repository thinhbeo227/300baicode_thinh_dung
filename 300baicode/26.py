import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

# Solution code here

from math import sqrt
a,b,c= map(int,input().split())
p= (a+b+c)/2
s=sqrt(p * (p - a)*(p-b)*(p-c))
r=(a*b*c)/(4*s)
print(f"{r:.3f}")