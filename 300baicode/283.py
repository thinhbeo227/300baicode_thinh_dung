n = int(input())
a = 0
for i in range(n):
    diem = float(input().split()[-1])
    if diem > a:
        a = diem
print(f"{a:.1f}")
