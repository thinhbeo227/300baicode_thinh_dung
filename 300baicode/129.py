a=int(input())
n=list(map(int,input().split()))
s=0
for i in range(a):
    s = s+n[i]
print(f"{s/a:.2f}")
