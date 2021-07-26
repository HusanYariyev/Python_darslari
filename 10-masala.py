a = input("Familiya kiriting: ")

if a[-2]=="o" and a[-3]=="p":
    a = a.replace(a[-1], " ")
    a = a.replace(a[-2], " ")
    print(a.replace(a[-3],"f"))

elif a[-2]=="o":
    print(a[0:len(a)-2])

elif a[-2]=="e":
    print(a[0:len(a)-3])

else:
    print("Familiyani to`g`ri kiritng!!!")