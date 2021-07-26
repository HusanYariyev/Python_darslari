
ism = input("Ismingizni kiriting ")
son = int(input("Necha martta takrorlasin "))

def takror(ism):

    if ism[len(ism)-1] != " " :
        ism = ism + " "
    else:
        ism = ism

    return lambda n : n * ism

x = takror(ism)

print(x(son))
