a = int(input("1-chegara "))
i = int(input("2-chegara "))
tartib = input("Juftmi toqmi? ")

if tartib == "juft" or tartib == "Juft":
    if a % 2 == 0:
        a = a
    else:
        a = a + 1
    while a <= i:
        print(a)
        a += 2
elif tartib == "toq" or tartib == "Toq":
    if a % 2 == 0:
        a = a + 1
    else:
        a = a
    while a <= i:
        print(a)
        a += 2
