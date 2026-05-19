v=int(input())
m=0
while v !=0:
    t= v%10
    v=v//10
    if t%2==1: # ? 3 % 2 = ?
        m=m+1
print(m)