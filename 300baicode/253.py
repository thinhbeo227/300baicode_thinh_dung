def perfect_number(n):
    tong = 0
    for i in range(1, n):
        if n % i == 0:
            tong += i
    return tong == n


g = int(input())

a = [int(input()) for _ in range(g)]
b = [j for j in a if perfect_number(j)]

if len(b) == 0:
    print("-")
else:
    print(*b)
