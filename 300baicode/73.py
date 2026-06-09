n=int(input())
m=int(input())
dem=0
for i in range (n ,  m+ 1):
    if i%3==0:
        dem=dem+1
print(dem)