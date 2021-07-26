x = int(input("Sonni kiriting "))

def qiymat(x):
    if x == 0:
        return 0
    elif x % 2 == 0:
        return 1
    elif x % 2 != 0:
        return -1
print(qiymat(x))
