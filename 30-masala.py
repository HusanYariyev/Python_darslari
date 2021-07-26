import math
a = (1,2,3,4,5,6,7,8,9,10)
b = list(a)
d = []
for i in range(1,len(b)+1):
    d.append(a[i-1])
    d.append(a[len(b)-i])
    if i==math.floor(len(b)/2):
        break
if len(b) % 2 == 1:
    d.append(math.ceil(len(b)/2))
print(tuple(d))