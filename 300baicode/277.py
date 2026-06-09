"""
diinh nghia 1 ham tinh dc do dai cua 1 doan thang
khi co toa do 2 diem

def chieu_dai(x1, y1, x2, y2):
    --> chieu dai
x = cd(xa, ya, xb, yb)
y
z
"""

import math


def cd(x1, y1, x2, y2):
    ac = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return ac


xa, ya, xb, yb, xc, yc = map(float, input().split())
AB = cd(xa, ya, xb, yb)
CA = cd(xc, yc, xa, ya)
BC = cd(xb, yb, xc, yc)
if (AB + BC > CA) and (AB + CA > BC) and (BC + CA > AB):
    CV = AB + BC + CA
    p = CV / 2
    S = 0.5 *(abs(xa * (yb - yc) + xb*(yc - ya) + xc*(ya - yb)))
    print(f"{CV:.1f} {S:.2f}")
else:
    print(-1)


# owr bai nay
