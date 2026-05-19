x=input()
x=x.split()
gtnn=len(x[0]) #
kt=x[0]
for y in x:
    if len(y)<gtnn:
        gtnn=len(y)
        kt=y
print(kt)
