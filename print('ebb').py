def find_gcd(a, b):
    r = a % b
    if r == 0:
        print ('НОД -', b)
    else:
        a = b; b = r
        find_gcd(a, b)

find_gcd(13, 12)