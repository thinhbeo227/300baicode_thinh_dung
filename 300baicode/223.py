w = int(input())
a = []
for i in range(w):
    g = list(map(int, input().split()))
    a.append(g)
# for i in range(w):
#     print(a[i][w-i-1],end=' ')


dong = 0
cot = w - 1


while 0 <= dong < w and 0 <= cot < w:
    print(a[dong][cot], end=" ")
    dong = dong + 1
    cot = cot - 1
