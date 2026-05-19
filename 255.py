def tong(n: int):
    return n * (n + 1) // 2

def stg(m: int):
    s = 1
    while tong(s) < m:
        s = s + 1
    return tong(s) == m


# print(tong(3))  # 1 + 2 + 3 = 6
# print(tong(5))  # 15

# print(stg(15))

n = int(input())

a = []
for i in range(n):
    c = int(input())
    if stg(c):
        a.append(c)


if len(a): 
    print(*a)
else:
    print("-")

# 0 : F
# 1 : T