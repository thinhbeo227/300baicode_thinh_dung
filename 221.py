dong, cot = map(int, input().split())
a = []
for i in range(dong):
    j = list(map(int, input().split()))
    a.append(j)
gtbn = float("inf")
d, c = -1, -1
for i in range(dong):
    for l in range(cot):
        if a[i][l] % 3 == 0 and a[i][l] < gtbn:
            gtbn = a[i][l]
            d, c = i, l
if gtbn == float("inf"):
    print(-1)
else:
    print(gtbn)
    print(d, c)
