n = int(input())
s = list(map(int, input().split()))
x = int(input())
b = []
for i in s:
    if i != x:
        b.append(i)
if len(b) == len(s):
    print("NO CHANGE")
elif len(b) == 0:
    print("EMPTY")
else:
    print(*b)