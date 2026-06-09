'''
4  = 2 * 2
16 = 4 * 4
25 = 5 * 5
36 = 6 * 6
81 = 9 * 9

sqrt(81) = 9
a = 25
x = int(sqrt(a)) = 5

if x * x == a:
    yes
else:
    no
----------------------
a = 10
x = int(sqrt(10)) = 3.16 = int(3.16) = 3
x * x !=
'''
# lam cai nay di =))
import math 
a=int(input())
if a < 0:
    print("No")
else:
    x=int(math.sqrt(a))
    if x*x==a:
        print("Yes")
    else:
        print("No")
