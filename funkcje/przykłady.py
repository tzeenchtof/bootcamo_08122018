# liczby = [1, 2, 3, 4]
#
# liczby2 = [5, 6, 7, 8]
#
# for i, l in enumerate(liczby):
#     print(f'indeks={i}, wartość={l}')
#
# def drukuj(lista):
#     for i, l in enumerate(lista):
#         print(f"Indeks={i}, wartość={l}")
#
#
# drukuj(liczby)
# drukuj(liczby2)
#
# a = 2
# b = 3
#
# def dodaj_a_b():
#     if a == 2:
#         return 4
#     wynik = a + b
#     return wynik
#
# print(dodaj_a_b(10, 20))
# wynik = dodaj_a_b(20, 50)
#
# print(wynik)
#
# print(a, b)
# print(globals())
# print(locals())


def wykonaj_operacje(operacja, *args):
    print(args)
    print(type(args))
    return operacja(args)


# print (wykonaj_operacje('a', 'b', 10, 20, 20, 30, 50))
# print (wykonaj_operacje('a', 'b', 10, 20, 20, 30, 50))

print (wykonaj_operacje(min, 10, 20, 20))
print (wykonaj_operacje(sum, 10, 20, 30, 50))
print (wykonaj_operacje(max, 10, 20, 20, 30, 50))


def napisy(*args, funkcja=None, funkcja2):

"""
Napisz funkcje, która przyjmuje dowolną liczbę napisów,
1. Zwróci te napiosypołączone znakiem nowej linii
>>> napisy("a", "b")
a
b

>>> napisy("a", "b", "d")

a
b
d

"""

    tekst = "\n".join(args)

    print(kwargs)
    for k in kwargs:
        tekst = kwargs[k] (tekst)

    return tekst

print("-"*40)
print(napisy("a", "b", "c"))

def upper(napis):
print("-"*40)
print(napisy("a", "b", "c", "d", funkcja=str.upper funkcja2=str.title))