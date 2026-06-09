def thc(a: list, n: int):
    for i in a:
        if i == n:
            return True
    return False


n = int(input())
s1 = list(map(int, input().split()))
m = int(input())
s2 = list(map(int, input().split()))
dem = 0
bhvd = []
for i in s1:
    if not thc(s2, i):
        bhvd.append(i)
        dem = dem + 1
if dem == 0:
    print("EMPTY")
else:
    print(*bhvd)
