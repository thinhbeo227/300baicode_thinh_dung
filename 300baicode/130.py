a=int(input())
n=list(map(int,input().split()))
s=0
for i in range(a):
    if n[i]%3==0:
       s=s+n[i]
print(s)
# 6 + 9 + 12 
# 15 + 12 = 