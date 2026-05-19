n,m=map(int,input().split())

dem=0
ton=0
for i in range (n ,  m+ 1):
    if i%2==0:
        dem=dem+1
        ton=ton+i

if dem==0:
    print(0)
else:
    print(int(ton/dem))
# 2 4 6 = 12
# dem = 3
# tong/dem
# 0 / 0