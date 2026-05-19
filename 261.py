def dao_ngc(n: int):
    kq = 0
    while n != 0:
        r = n % 10  # tasch hang don vi
        kq = kq * 10 + r  # nhet vao kq
        n = n // 10
    return kq
def xu_ly(n):
    if n > 0:
        return dao_ngc(n)
    return -1 * dao_ngc(abs(n))
uia=int(input())
a=[]
for i in range(uia):
    a.append()