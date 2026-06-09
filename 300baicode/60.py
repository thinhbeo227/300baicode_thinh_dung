n = input()
gtln = n[0] # lay gia tri dau tien?
gtnn = n[0] # '2'
for i in n:
    if int(i) > int(gtln):
        gtln = i 
    if int(i) < int(gtnn):
        gtnn = i 
print(f'{gtln} {gtnn}')