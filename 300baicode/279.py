n = int(input())
stduents = []
for i in range(n):
    row = input()
    ho_ten, lop, tuoi, diem = row.split("|")
    stduents.append((ho_ten, lop, int(tuoi), float(diem)))
n_nhat = stduents[0]
for student in stduents:
    if n_nhat[2] > student[2]:
        n_nhat = student  
# print(n_nhat[0])


print(stduents)