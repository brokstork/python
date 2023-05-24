def find_gcd(a, b):
    r = a % b
    if r == 0:
        print('НОД -', b)
    elif r == 1:
        print('НОД - 1')
    else:
        a = b; b = r
        find_gcd(a, b)
find_gcd(56, 32)