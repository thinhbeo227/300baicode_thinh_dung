h=list(input())
h[0] = h[0].upper()
for i in range(1, len(h)):
    h[i]=h[i].lower()
print(*h,sep="")