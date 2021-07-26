shaxs = {
    "ism" : "Husan",
    "yosh" : 10,
    "o`quvchi" : True
}
yil = int(input("yilni kiriting "))

shaxs["yosh"] = shaxs["yosh"] + yil
if shaxs["yosh"] < 18:
    print(shaxs)
else:
    shaxs["o`quvchi"] = False
    print(shaxs)