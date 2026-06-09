import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

# n=int(input())
# for i in range(n):
#     x,y=map(int,input().split())
#     print(x**y,end=" ")
    
'''
máy chấm nó sẽ chia input và output
'''



















import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

uia=int(input())
for u in range(uia):
    uui,iia=map(int,input().split())
    print(uui**iia,end=" ")