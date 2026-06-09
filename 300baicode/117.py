'''
Số nguyên tố là số như nào?
'''
# def snt(n):
#     for i in range(2, n):
#         # nếu như tìm được 1 ước nào nữa khác 1 & n 
#         # --> ko phải snt 
#         # --> kết luận ko phải snt
#         if n % i == 0:
#             return False
    
#     # nếu như kết thúc vòng lặp mà ko tìm được ước nào khác
#     # ngoài 1 & chính nó
#     # --> đây là snt
#     return True


# m = int(input())
# n = int(input())
# for i in range(m, n + 1):
#     if snt(i):
#         print(i, end=' ')

def ngt(n):
    if n < 2: return False
    for i in range(2,n):
        if n %i==0:
            return False
    return True

def tong(n):
    s = 0
    for i in range(1, n + 1):
        s = s + i 
    return s

if __name__ == '__main__':
    a=int(input())
    b=int(input())

    for i in range(a,b+1):
        if ngt(i):
            print(i,end=" ")
        