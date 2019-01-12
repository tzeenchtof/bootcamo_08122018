# Napisz funkcję zwracającą zbiór wszystkich znaków
# występujących w napisie więcej niż zadana liczba razy
# przykład użycia:
# wiecej_niz('ala ma kota a kot ma ale', 3)
# {'a', ' '}

def wiecej_niz(napis, prog):
    # wynik = set()
    # unikalne = set(napis)
    # for c in unikalne:
    #     if napis.count(c) > prog:
    #         wynik.add(c)
    # return wynik

    return {x for x in set(napis) if napis.count(x) > prog}

def potega(podstawa, wykladnik=2):
    return podstawa ** wykladnik

print(potega(4, 3))
print(potega(4, 2))
print(potega(4))

def test_wiecej_niz():
    assert wiecej_niz('ala ma kota a kot ma ale', 3) == {"a", ' '}

def test_wiecej_niz_dla_pustego_napisu():
    assert wiecej_niz('', 3) == set()



# test do zadania
# pip install pytest - instalacja frameworka do testów - wpisać w Terminal
assert wiecej_niz('ala ma kota a kot ma ale', 3) == {"a", ' '}