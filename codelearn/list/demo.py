'''
5
502
123
4
3
2
'''
a = []

n = int(input()) # 5
# input
for i in range(n):
    x = int(input())
    a.append(x)

# sap xep
a.sort()

# output
# a = [5, 1, 4, 3, 2]
for i in range(n):
    print(a[i], end=' ')