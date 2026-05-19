n=int(input())
tong=0
for i in range(n):
    u=input()
    diem = u.split()[-1]
    diem = float(diem)
    tong=tong+diem
print(f"{tong/n:.2f}")