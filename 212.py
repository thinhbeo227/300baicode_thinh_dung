n = int(input())
names = [input() for i in range(n)]

names.sort(key=lambda full_name: (
    full_name.split()[-1],              # tên (ưu tiên)
    " ".join(full_name.split()[:-1])    # phần còn lại (họ + tên đệm)
))

print(*names,sep="\n")