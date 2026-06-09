n=int(input())
A=list(map(int,input().split()))
dc=0
dl=0
tc=0
tl=0
for i in range(len(A)):
    if A[i]%2==0:
        dc+=1
        tc=tc+A[i]
    else:
        dl=dl+1
        tl=tl+A[i]
print(dc)
print(dl)
print(tc)
print(tl)
