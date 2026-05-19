a=int(input())
if a<18:
    print("Tre em")
    if a<=6:
        print("Tre mam non")
    if 7<= a<=11:
        print("Tre tieu hoc")
    if 12<= a<=17:
        print("Tre trung hoc")
if 18<= a<60:
    print("Nguoi truong thanh")
    if 18<= a<=23:
        print("Sinh vien")
    if 24<= a<60:
        print("Nguoi di lam ")
if a>=60:
    print("Nguoi cao tuoi")
    if 60<= a<=62:
        print("Sap nghi huu")
    if 62<a:
        print("Da nghi huu")