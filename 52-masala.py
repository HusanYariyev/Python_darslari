try:
    son = int(input("Sonni kiriting "))
    if son < 0 :
        raise Exception()
except:
    print("Xato")
else:
    print("Xato yo`q")
