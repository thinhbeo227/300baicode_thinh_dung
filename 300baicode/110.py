def snt(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def chen(n):
    return snt(n) and snt(n + 2)


n = int(input())
if chen(n):
    print("Yes")
else:print("No")