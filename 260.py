def dem_uoc(n):
    d = 0
    for i in range(1, n + 1):
        if n % i == 0:
            d = d + 1
    return d


r = int(input())
a = [abs(int(input())) for _ in range(r)]
for i in a:
    print(dem_uoc(i), end=" ")
