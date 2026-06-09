n = int(input())
A = []
for i in range(n):
    id, name, year, gt, v, t, a = input().split("|")
    A.append((id, name, year, gt, v, t, a))
    
    
    


A.sort(key=lambda x: (x[1].split()[-1], x[1].split()[0], -int(x[5])))
for hs in A:
    print("|".join(hs))

# x[1].split()[-1] tai sao lai la ten

'''
HS01|Tran Phi An Binh|2005|Nu|7|8|6

x[1].split()[-1]>> = Tran Phi An Binh
'''
