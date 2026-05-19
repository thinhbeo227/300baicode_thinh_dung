n,m=map(int,input().split())


ton=0
for i in range (n ,  m+ 1):
    if i%2==0:
        ton=ton+i
print(ton)