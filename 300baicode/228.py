m, n, k = map(int, input().split())
a = []
for _ in range(m):
    x = list(map(int, input().split()))
    a.append(x)
    
# diem ma matrix dc input xong
for dong in a:
    dong.pop(k)
for dong in a:
    print(*dong)
