# s1 = "Tran Phi Anh Binh"
# s2 = "Tien Giang"
# k = 8
# """
# insert s2 vao vi tri k cua s1
# """
# # start: end - 1

# kq = s1[:k] + s2 + s1[k:] 
# print(kq)
TNT1=input()
TNT2=input()
k=int(input())
TNT3= TNT1[:k]+TNT2+TNT1[k:]
print(TNT3)