x,n=map(int,input().split())
j97=0
while x !=0:
    r=x%10
    x=x//10
    if r>n:
        j97=j97+r
print(j97)