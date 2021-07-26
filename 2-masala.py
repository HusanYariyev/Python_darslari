import math

a = int(input("a =  "))
b = int(input("b =  "))
c = int(input("c =  "))

peremetr = a + b + c

p = peremetr / 2
s =  math.sqrt(p*(p-a)*(p-b)*(p-c))

print(f"Yuzasi= {s} , Peremetri= {peremetr}")


