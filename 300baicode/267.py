def findMax(a: list):
    vt = 0
    sln = a[0]
    for i in range(len(a)):
        if sln < a[i]:
            sln = a[i]
            vt = i
    return sln, vt


def findMin(a: list):
    vt = 0
    sbn = a[0]
    for i in range(len(a)):
        if sbn > a[i]:
            sbn = a[i]
            vt = i
    return sbn, vt


n = int(input())
a = []

for i in range(n):
    x = list(map(int, input().split()))
    gtln, vt = findMax(x)
    gtnn, vtn = findMin(x)
    print(f"Max: {gtln}, Vi tri Max: {vt}; Min: {gtnn}, Vi tri Min: {vtn}")
