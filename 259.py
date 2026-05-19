def tong_uoc(n: int):
    tong = 0
    for i in range(1, n + 1):
        if n % i == 0:
            tong = tong + i
    return tong


n = int(input())

a = [abs(int(input())) for _ in range(n)]

for x in a:
    print(tong_uoc(x), end=" ")
