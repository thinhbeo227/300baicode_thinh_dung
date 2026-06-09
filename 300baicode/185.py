# upper: viết hoa

# up: lên
a = input()
"""
chỉ cần 1 ký tự
ko phải viết hoa
--> no
    dừng lại luôn?
    
yes
"""
dem_chu_thuong = 0
for i in a:
    if i.islower():
        print("NO")
        dem_chu_thuong += 1
        break
if dem_chu_thuong == 0:
    print("YES")
