def hkt(v):
    ton = 0
    for i in range(1, v):
        if v % i == 0:
            ton =ton +i
    return ton > v
v=int(input())
if hkt(v):
    print("Yes")
else:
    print("No")

