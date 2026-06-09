import sys

sys.stdin = open("input.txt", "r")

n = int(input())

ds = []

for i in range(n):
    c = input()
    diem = float(c.split()[-1])
    ho_ten = c.split()[:-1]
    ho_ten = " ".join(ho_ten)
    ds.append((ho_ten, diem))


for x, y in ds:
    y = y + 1
    print(x, y)
