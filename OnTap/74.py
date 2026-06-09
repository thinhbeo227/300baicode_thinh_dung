m=int(input())
n=int(input())
g=0
for i in range(m,n+1):
    if i%2==0:
        g=g+1
        print(i)
if g==0:
    print("-")
