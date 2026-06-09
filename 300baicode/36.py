a, b = map(float,input().split())
z=(a+b*2)/3
print(f"{z:.1f}")
if z>=8:
    print("Gioi")
elif z>=6.5:
    print("Kha")
elif z>=5.0:
    print("Trung binh")
elif z>=3.5:
    print("Yeu")
else:
    print("Kem")                                                            