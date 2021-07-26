# maxsus masala:
a1 = []
shaxslar = [
    {
        "ism": "Shoxzod",
        "yoshi": 20,
        "jinsi" : "erkak"
    },
    {
        "ism": "Oybek",
        "yoshi": 22,
        "jinsi" : "erkak"
    },
{
        "ism": "Bunyod",
        "yoshi": 22,
        "jinsi" : "erkak"
    },
    {
        "ism": "Madinabonu",
        "yoshi": 13,
        "jinsi" : "ayol"
    }
]

for i in shaxslar:
    if i["jinsi"] == "erkak":
        i["Familiyasi"] = i["ism"]+"ov"
    else:
        i["Familiya"] =i["ism"]+"yeva"
    print(i)
