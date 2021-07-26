
def yigindi(a,b):
    return lambda n : (a + b) ** n

x = yigindi(2,3)

print(x(2))
