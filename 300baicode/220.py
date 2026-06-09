import sys

sys.stdin = open("input.txt", "r")

dong, cot = map(int, input().split())
a = []
t = 0
# nhap
for i in range(dong):
    n = list(map(int, input().split()))
    a.append(n)

d, c = -1, -1

# am = -9999
am = float('-inf')
for i in range(dong):
    for j in range(cot):
        # chỉ cập nhật. nếu tm dk
        if a[i][j] < 0 and a[i][j] > am:
            am = a[i][j]
            # tt = [i, j]
            d, c = i, j

if am != float('-inf'):
    print(am)
    print(d, c)
else:
    print(0)
