a = int(input("1-son "))
b = int(input("2-son "))

def kattasi(a,b):
    if a>b:
        return a
    else:
        return b
print(kattasi(a,b))