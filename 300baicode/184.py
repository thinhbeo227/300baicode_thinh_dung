a=input()
for b in a:
    if b.isalpha()and not b.islower():
        print("NO")
        break
else:print("YES")
