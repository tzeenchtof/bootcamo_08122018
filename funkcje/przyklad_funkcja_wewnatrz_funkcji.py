


def a():
    print("jestem w ifunkcji a")
    def int(x=None):
        if x:

            return 10
    def b():
        print("jestemw wfunkcji b!")

    def c():
        print("jestemw wfunkcji c!")
    print (locals())
    print (globals())
    b()
    c()
    print(int())

print(int())
a()

def pobierz_dane():
    print("pobrałem dane")

def loguj_uzycie(func):
    """ to będzie dekorator. wypisze tekst przed i po uruchomieniu funkcji"""

    def wrapper(*args, **kwargs):
        print("to się wykona przed")
        func(*args, **kwargs)
        print("to się wykona po")
        return f"Wynik: {func(*args, **kwargs)}"
    return wrapper
@loguj_uzycie
def potega(podstawa, wykladnik):
    wynik = podstawa ** wykladnik

    return wynik

def pobierz_dane():
    print("pobrałem dane")

print("bez dekoratora")
pobierz_dane()

print("udekorowane")
pobierz_dane = loguj_uzycie(pobierz_dane)
pobierz_dane()

potega
