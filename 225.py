w = int(input())
a = []
b=[]
snn=float("inf")
for i in range(w):
    g = list(map(int, input().split()))
    a.append(g)
for i in range(w):
    b.append(a[i][w-i-1])
for i in b:
    if i%2==0 and snn>i:
        snn=i
if snn==float("inf"):
    print(-1)
else:
    print(snn)