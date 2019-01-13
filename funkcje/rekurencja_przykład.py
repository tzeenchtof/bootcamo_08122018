lista = [10, 20, 30, 40]

def rekuprint(lista):
    if len(lista) == 1:
        print(lista[0])
    else:
        print(lista[0])
        rekuprint(lista[1:])

rekuprint(lista)

def powieksz_o_jeden(liczba):
    liczba += 1
    print(liczba)
    powieksz_o_jeden(liczba)

powieksz_o_jeden(1)

def dodaj(liczba):
    """ Będzie dodawać do siebie wszystkie liczby od 1 do liczba"""
    if liczba == 0:
        return 0
    else:
        return liczba + dodaj(liczba-1)
print("Wynik", dodaj(5))

def hello();
    return('Hi!')

def goodmorning():
    return good norninhg
def sprawdz_czy_podzielna_przez_2_i_3(x):
    return x%2 == 0 and x%3 == 0


def sprawdz_czy(x, funkcja1, funkcja2):
    return funkcja1(x) and funkcja2(x)

print(sprawdz_czy(12, sprawdz_czy_podzielna_przez_2_i_3, lambda x: x > 5))
