n,x = map(int,input().split())
s=0
while n!=0:
    r = n%10
    n = n//10

    if r > x:
      s=s+r
print(s)