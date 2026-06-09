import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

def luythua(a: int) -> int:
    b: int=1
    for i in range(1,a+1):
        b=b*i
    return b

a=int(input())
n=[]
for i in range(a):
    n.append(int(input()))
for i in range(a):
    print(luythua(n[i]),end=" ")

