import math

y = float(input("Y= "))
h = float(input("H= "))
A = (math.tan(math.pow(y,3)-(math.pow(h,4)))+math.pow(h,2))/(pow(math.sin(h),2)+y)
print(A)