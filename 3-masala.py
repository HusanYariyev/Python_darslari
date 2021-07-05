import math

a = int(input("a =  "))
b = int(input("b =  "))

burchak = int(input("burchak =  "))

c = math.sqrt(pow(a,2)+pow(b,2)-(2 * a * b * math.cos(burchak * math.pi/180)))

print(f" c = {round(c)}")