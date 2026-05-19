n, m = map(int, input().split())
a = []
for _ in range(n):
    row = list(map(int, input().split()))
    a.append(row)

s = 0
# for row in a:
#     for i in row:
#         if i % 2 == 0:
#             s += i

for i in range(n):
    for j in range(m):
        if a[i][j] % 2 == 0:
            s += a[i][j]
            
print(s)


# 3 4 ==> 12