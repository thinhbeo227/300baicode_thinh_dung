row, col = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(row)]

min_sum, idx_col = float('inf'), -1
for x in range(col):
    s = 0
    for y in range(row):
        s += a[y][x]
    if s < min_sum:
        min_sum = s
        idx_col = x 

print(idx_col)
print(min_sum)


