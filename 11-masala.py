yil = int(input("Yilni kiriting: "))

if yil % 4==0 and (yil%100)%400!=0:
    print("Kabisa yili")
else:
    print("Kabisa yili emas ")
