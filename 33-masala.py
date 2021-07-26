# maxsus masala:
shaxslar = [
    {
        "ism": "Alisher",
        "yoshi": 20
    },
    {
        "ism": "Oybek",
        "yoshi": 22
    },
    {
        "ism": "Bunyod",
        "yoshi": 22
    },
    {
        "ism": "Madinabonu",
        "yoshi": 13
    }
]

for shaxs in shaxslar:
    a = shaxs["ism"]
    if a[0] == "A" or a[0]== "a" :
        print(shaxs["ism"])