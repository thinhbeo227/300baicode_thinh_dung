'''
1. ước là gì?
6: 1 2 3 6
13: 1 13 --> 2
21: 1 3 7 21 --> 4

3: 1 3
5: 1 5
7: 1 7
Những số có chính xác 2 ước thì đc gọi là snt

for: 1->n
    n % i == 0: dem ++
print(dem)

8: 1 2 4 8 --> 4    
'''
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

# Solution code here

n=int(input())
dem=0
for i in range(1,n+1):
    if n % i==0:
        dem=dem+1
print(dem)
