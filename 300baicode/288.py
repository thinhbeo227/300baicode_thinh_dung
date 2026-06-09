u = int(input())
a = list(map(int, input().split()))
n = int(input())
dem = 0
for i in a:
    if i == n:
        dem = +1
if dem == 0:
    print("NO")
else:
    print("YES")