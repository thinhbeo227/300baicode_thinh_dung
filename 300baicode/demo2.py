k = int(input())
dem = 0
i = 0
while True:
    if i % 2 == 0:
        print(i, end=' ')
        dem += 1
    if dem == k: break
    i += 1
