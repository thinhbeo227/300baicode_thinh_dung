# def tong_cs(n):
#     s = 0
#     while n != 0:
#         r = n % 10
#         s += r
#         n //= 10
#     return s


# a = list(map(int, input().split())) # [12, 34, 56,  78]

# b = [tong_cs(x) for x in a]         # [3,  7,  11,  15]


# for x, y in zip(a, b):
#     print(x, y)

# '''
# 12 3
# 34 7
# 56 11
# 78 15
# '''

# print(tong_cs(12345))



# 123 = s + 3 = 3
# 12 => s + 3 + 2
# 1 => s + 3 + 2 + 1
# 0
def tong(g):
    h=0
    while g !=0:
        m=g %10
        h=h+m
        g=g//10
    return h
a=list(map(int,input().split()))
b=[]
for h in a:
    b.append(tong(h))
for g,h in zip(a,b):
    print(g,h)