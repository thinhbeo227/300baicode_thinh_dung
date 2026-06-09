N=int(input())
A=list(map(int,input().split()))
x=int(input())
dem1=0
dem2=0
for i in range(len(A)):
    if x>A[i]:
        dem1+=1
    elif x<A[i]:
        dem2+=1
print(dem1)
print(dem2)