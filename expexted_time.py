from math import sqrt
def answer(n):
    return pad_count(n)

def pad_count(n):
    print n
    if n <=3:
        return n
    else:
        sqrt_n = int(sqrt(n))
        return 1 + pad_count(n-sqrt_n**2)


        