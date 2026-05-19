a=input()
b=input()
for i in range(len(a)):
    if a[i] == b: # gap ky tu ko can thi bo qua
        continue
    print(a[i], end='')