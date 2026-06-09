m,n=map(int,input().split())
j97=0
d1=0
d2=0
for i in range(m,n+1):
    if i%7==0:
        j97=j97+1

for i in range(m,n+1):
    if i%2==0 or i%3==0:
        d1=d1+i
        d2=d2+1
print(j97,end=" ")

if d2==0:
    print(0.0)
else:
    print(f"{d1/d2:.1f}")

# d2 = 0????
