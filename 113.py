def x(n): 
    i = 0
    while i * (i + 1) < n:
         i += 1
    return i * (i + 1) == n
y=int(input())
if x(y):
    print("Yes")
else:
    print("No")
