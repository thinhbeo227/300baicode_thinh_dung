n=int(input())
v=0
while n != 0:
    r=n%10
    n=n//10
    if r%2==0:
        v=v+r
print(v)