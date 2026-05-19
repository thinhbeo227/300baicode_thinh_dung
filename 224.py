dong = int(input())
a = []
b = []
ln = float("-inf")
for i in range(dong):
    x = list(map(int, input().split()))
    a.append(x)
for i in range(dong):
    b.append(a[i][i])

print(max(b))

# print(max(list(a[i][i] for i in range(dong))))
