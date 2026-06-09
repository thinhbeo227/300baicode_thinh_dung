def check(a: str):
    if a[0].islower():
        return False
    for i in range(1, len(a)):
        if a[i].isupper():
            return False
    return True
    # khi maf ta

'''
Tran

for w in s[1:]
'''

s = input()
s = s.split()
tm = True  
# for i in range(len(s)):
#     if not check(s[i]):
#         tm = False
#         break

for w in s:
    if not check(w):
        tm = False
        break
if tm:
    print("Yes")
else:
    print("No") 
