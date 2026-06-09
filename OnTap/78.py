m,n=map(int,input().split())
j97=0
d1=0
d2=0
for i in range(m,n+1):
    if i%5==0:
        j97=j97+i

for i in range(m,n+1):
    if i%6==0:
        d1=d1+i
        d2=d2+1
print(j97,end=" ")

if d2==0:
    print(0)
else:
    print(f"{d1//d2:.0f}")

# d2 = 0????