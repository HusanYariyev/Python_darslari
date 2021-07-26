import math
a = int(input("Enini kiriting "))
b = int(input("Bo`yini kiriting "))

def yuza(c):
    return lambda v : a * b * c

print(yuza(3)(3.14))
