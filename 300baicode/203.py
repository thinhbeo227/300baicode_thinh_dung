uia = input()
s = 0
sbn = "r"
for i in uia:
    if i != " " and ord(i) < ord(sbn):
        sbn = i
        s = ord(i)
print(f"{sbn}: {s}")


# lam 209