# qwertyuiop=input()
# for asdfghjkl in qwertyuiop:
#     if asdfghjkl.islower():
#         print(asdfghjkl.upper() ,end="")
#     else:
#         print(asdfghjkl.lower() ,end="")
        
def w(a:str):
    b=[]
    for i in a:
        if i.islower():
            b.append(i.upper(), )
        else:
            b.append(i.lower(), )
    return "".join(b)
# a=input()
# print(w(a))


print(w("Vuong Duy Nguyen"))

