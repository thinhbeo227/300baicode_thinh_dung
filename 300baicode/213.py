n=int(input())
a=[]
for i in range(n):
    a.append(input())
a=sorted(a, key=len)
print(*a,sep="\n")