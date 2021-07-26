import sys
try:
    i = int(input("Sonni kiriting "))
    if i % 2 == 0:
        i = i/0
    else:
        print("Dastur to'g'ri ishladi")
except:
    print(sys.exc_info()[1])
finally:
    print("Dastur tugadi")