import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

n=int(input())
a=[]

for i in range(n):
    x=int(input())
    a.append(x)#them x vao a
q=0
k=int(input())
for i in range(n):
    if a[i]==k:
        print("Yes")
        print(i)
        q=1
        break
if q==0:
    print("No")