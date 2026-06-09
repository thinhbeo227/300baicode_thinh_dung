
'''
a b c
3 | 5 | 1

b_a = ceil(a / 2) = ceil(1.5) = 2
b_b = ceil(b / 2) = 3
b_c = 1



'''

# a,b,c=map(int,input().split())
import math 
a,b,c=map(int,input().split())
a= math.ceil(a/2)
b= math.ceil(b/2)
c= math.ceil(c/2)
print(a+b+c)
