# Написать функцию перевода десятичного числа в двоичное и обратно, без
# использования функции int

def bi(x, b=""):
    while x > 0:
        b = str(x % 2) + b
        x = x // 2
    print(b)

print(bi(2))

def convert_to(number, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return result.upper() if upper else result

print(convert_to(4, 2))