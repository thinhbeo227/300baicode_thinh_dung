n,m=map(int,input().split())
dem=0
for i in range (n ,  m+ 1):
    if i%2==0:
        dem=dem+1
print(dem)
