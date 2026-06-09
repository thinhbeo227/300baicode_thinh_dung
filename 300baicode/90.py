u=int(input())
p=0
while u !=0:
    y=u%10
    u=u//10
    p=p*10+y
print(p)