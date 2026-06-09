import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

# Solution code here
a=int(input())
d=0
for i in range(1,a+1):
    if a%i==0:
        d += 1

'''
6
1 2 3 4 5 6
x x x     x 

7: 1 7
5: 1 5
'''