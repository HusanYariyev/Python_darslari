a = input("Ismni kiriting: ")
unli = ["a", "o", "u", "i", "e"]
if a[-1]=="a" or "o" or "u" or "i" or "e":
    print(a+"ov")
elif a[-1]=="n":
    print(a+"ov")
else:
    print(a+"yev")
if a[-1]=="f":
    print(a.replace(a[-1],"p")+"ov")
