'''
for i in range(m, n):
    if snt(i):
        d++
'''

def uia(x):
    if x < 2: 
        return False
    for i in range(2,x):
        if x %i ==0:
            return False
    return True

dem=0
m=int(input())
n=int(input())

for i in range(m,n + 1):
    if uia(i):
        dem=dem+1
print(dem)