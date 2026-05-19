# tinh tong cac so tu 1 -> n
'''
2 + 4 + 6 ... + n

s   = 2 + 4
dem = 2
6 / 2 = 3b

'''
# n = 5
# tong = 0
# dem = 0
# for i in range(1, n + 1):
#     if i % 2 == 0:
#         tong = tong + i # tinh tong
#         dem = dem + 1
# print(tong / dem)

n: int = int(input())

tong: float = 0
dem: int = 0


for i in range(1, n + 1):
    if i % 5 == 0:
        tong = tong + i 
        dem = dem +1
print(tong / dem)