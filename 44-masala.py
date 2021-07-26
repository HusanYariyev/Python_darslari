a = int(input("Sonni kiriting "))

def modul(a):
    if a>0:
        return a
    else:
        return -a


def ikkila(a):
    return 2*a


def masala(a):
    a = modul(a)
    return ikkila(a)

print(masala(a))

