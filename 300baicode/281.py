import sys

sys.stdin = open("input.txt", "r")
sys.stdout = open("output.txt", "w")


n = int(input())
a = []

for i in range(n):
    c = input()
    # *ho_ten, diem = c.split()
    diem = c.split()[-1]
    ho_ten = c.split()[:-1]
    ho_ten = " ".join(ho_ten)
    diem = float(diem)
    # print(ho_ten, diem)
    print(f"{ho_ten} {diem:.1f}")
