def uio(n: int) -> int:
    return n * (n + 1) // 2


def hpde(m: int) -> bool:
    gh = 1
    while uio(gh) < m:
        gh += 1
    return uio(gh) == m


n = int(input())
if hpde(n):
    print("Yes")
else:
    print("No")

# print(hpde(n))

# print(uio(3)) # int: 6