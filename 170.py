# TNT=input()
# k=int(input())
# s = TNT[:k] + TNT[k + 1:]# abc + [d]ef = abcef
# print(s)


s = "abcdef"
s2 = "_____________________"
k = 2 # c

# s[start:end] start end - 1
# s[1:4] bcd 1 - 3
# s[2:6] cde

kq = s[:k] + s[k + 1:]# ab + [c]def
print(kq)