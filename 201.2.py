import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')
# n = int(input())

# a = [input() for _ in range(n)]
# print(a)
# kq = ""
# for x in a:
#     if len(x.strip()) == 0:
#         kq += " "
#     else:
#         kq += x
# print(kq)











































y=int(input())
x=[input() for _ in range(y)]
kq = ""
for gugugaga in x:
    if len(gugugaga.strip()) == 0:
        kq += ""
else:
    kq += gugugaga
print(kq)
