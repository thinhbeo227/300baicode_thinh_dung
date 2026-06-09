from math import gcd


def rg(t, m):
    x = gcd(t, m)
    t = t // x
    m = m // x
    if m < 0:
        m *= -1
        t *= -1
    return t, m


def congtcps(t1, m1, t2, m2):
    t = t1 * m2 + t2 * m1
    m = m1 * m2
    return rg(t, m)


def hieuaips(t1, m1, t2, m2):
    t = t1 * m2 - t2 * m1
    m = m1 * m2
    return rg(t, m)


def tichaips(t1, m1, t2, m2):
    t = t1 * t2
    m = m1 * m2
    return rg(t, m)


def thuongaips(t1, m1, t2, m2):
    t = t1 * m2
    m = t2 * m1
    return rg(t, m)


t1, m1 = map(int, input().split())
t2, m2 = map(int, input().split())
print(*rg(t1, m1))
print(*rg(t2, m2))
print(*congtcps(t1, m1, t2, m2))
print(*hieuaips(t1, m1, t2, m2))
print(*tichaips(t1, m1, t2, m2))
print(*thuongaips(t1, m1, t2, m2))


