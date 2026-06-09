dong, so = map(int, input().split())
a = []
t = 0
# nhap
for i in range(dong):
    n = list(map(int, input().split()))
    a.append(n)

s = 0
for row in a:
    for x in row:
        s += x 
        
print(s)