n = int(input())
names = [input() for i in range(n)]
mark = [float(input()) for _ in range(n)]
for ten, diem in zip(names, mark):
    print(f"{ten}: {diem:.1f}")
# ctrl + d
# double
# refactor: tái cấu trúc
# vd mình đổi n --> names
# thì nó sẽ thay đổi trong toàn bộ code

# ctrl + ` --> theme


