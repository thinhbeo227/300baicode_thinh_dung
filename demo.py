s = "Tran Phi An Binh"

s = s.split() # ['Tran', 'Phi', 'An', 'Binh']

chieu_dai_nn = len(s[0]) # 4
kt = s[0] # tran

for x in s:
    if len(x) < chieu_dai_nn:
        chieu_dai_nn = len(x)
        kt = x 
        
print(kt)
        