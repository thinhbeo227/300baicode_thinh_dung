dong, cot, xoa = map(int, input().split())
a = []

for i in range(dong):
    c = list(map(int, input().split()))
    a.append(c)
# for i in range(dong):
#     if i == xoa:
#         continue
#     print(*a[i])


a.pop(xoa)

for dong in a:
    print(*dong)
