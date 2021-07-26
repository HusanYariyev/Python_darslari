import math

def aylana(r):
    return lambda s : r ** 2 * math.pi

yuza = aylana(2)

print(math.floor(yuza(3.14)))