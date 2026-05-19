def find_min_even_digit(n):
    min_even_digit = float('inf') # 10
    while n != 0:
        digit = n % 10
        if digit % 2 == 0 and digit < min_even_digit:
            min_even_digit = digit
        n //= 10
    return min_even_digit if min_even_digit != float('inf') else -1
if __name__ == '__main__':
    n = int(input())
    min_even_digit: int = find_min_even_digit(n)
    if min_even_digit == -1: print("-")
    else: print(min_even_digit)
