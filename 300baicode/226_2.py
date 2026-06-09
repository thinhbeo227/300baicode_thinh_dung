dong, cot = map(int, input().split())
a = []
b = float("-inf")
c = 0
for i in range(dong):
    # day la 1 dong
    j = list(map(int, input().split()))
    # append tong(j)
    a.append(sum(j))
for i in range(len(a)):
    if b <= a[i]:
        b = a[i]
        c = i
print(c)
print(b)

