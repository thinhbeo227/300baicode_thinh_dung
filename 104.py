import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

# Solution code here
'''
i: 1->9
f'{i} * {n} = {i * n}'
'''
u=int(input()) 
for i in range(1,10,1):
    print(f'{i} x {u} = {i * u}')