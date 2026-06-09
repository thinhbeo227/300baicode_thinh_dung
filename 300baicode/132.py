
a=int(input())

# n=list(map(int,input().split()))

n = []
for i in range(a):
    n.append(int(input()))

s=0
dem=0
for i in range(a):
    if n[i]%2==0:
        dem=dem + 1
        s= s + n[i]

if dem==0:
    print("0.000")
else:
    print(f'{s/dem:.3f}')