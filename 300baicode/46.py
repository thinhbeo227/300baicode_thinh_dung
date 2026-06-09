a =input()
s = 0
for i in a:
    s = s + int(i)
x = s % 10
print(x)
if x==9:
    print("Yes")
else:
    print("No")