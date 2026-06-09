ten = input()
ss = 0
sln = "0"
for i in ten:
    if i != " " and ord(i) > ord(sln):
        sln = i
        ss = ord(i)
print(f"{sln}: {ss}")


# ten = ten.split()
# an = []
# for i in ten:
#     for j in range(len(i)):
#         an.append(i[j])
# ss = 0
# sln = "0"
# for i in an:
#     if ord(i) > ord(sln):
#         sln = i
#         ss = ord(i)
# print(f"{sln}: {ss}")
