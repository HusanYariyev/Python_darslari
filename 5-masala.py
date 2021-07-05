import math

y = float(input("Y= "))
x = float(input("X= "))
a = float(input("A= "))

G = (pow(math.cos(2*abs(y-x)-(x+y)),(4*pow(x,2))))/(pow(math.atan(x+a),4)+pow(x,5))

print(G)