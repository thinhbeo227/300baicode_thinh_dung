N=int(input())
A=list(map(int,input().split()))
snn=99999
dem=0
for i in range(len(A)):
    if A[i]<=snn:
        snn=A[i]
for i in range(len(A)):
    if A[i]==snn:
        dem+=1
print(dem)
# dem xem co bn gia tri = gtnn
# 5
# 28 28 28 28 29
'''
snn = 28
d = 0
for i in range(len9a):
    if a[i] == snn:
        d += 1
'''