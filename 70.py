n: int = int(input())

tong: float = 0
dem: int = 0


for i in range(1, n + 1):
    if i % 5 == 0 and  i % 3 == 0:
        tong = tong + i 
        dem = dem +1
print(tong / dem)