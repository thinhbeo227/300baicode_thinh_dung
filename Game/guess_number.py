import random
import os

os.system("cls")

x = random.randint(1, 100)
n = 0
max_turn = 7

while n < max_turn:
    b = input("Nhập số (1-100) hoặc q để thoát: ")
    if b.lower() == "q":
        print("👋🏻 chicken ")
        break
    
    try:
        b = int(b)  # "5" -> 5
    except:
        print("⚠️ Nhập sai! Vui lòng nhập số.")
        continue

    n += 1

    os.system("cls")

    if b < x:
        print("Số", b, "của bạn <BÉ> hơn")
    elif b > x:
        print(f"Số {b} của bạn <LỚN> hơn")
    else:
        print(f"🎉 Bạn thắng sau {n} lần!")
        break

    if abs(b - x) <= 5:
        print("🔥 Rất gần rồi!")
    if abs(b - x) >= 20:
        print("Chưa Tày Đâu xa qua'")
    print(f"Còn {max_turn - n} lượt")

if b != x:
    print(f"❌ Bạn thua! Số đúng là {x}")
