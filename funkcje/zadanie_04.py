# zaimplementuj funkcję formatującą podane napisy
# przykład użycia:
# >>> formatuj(
#     'koszt $cena PLN',
#     'kwota $cena brutto',
#     cena=10,
#     )
# 'koszt 10 PLN\nkwota 10 brutto'

def formatuj(*napisy, **zmienne):
    napis = "\n".join(napisy)
    for zmienna in zmienne:
        napis = napis.replace(f"{zmienna}", zmienne[zmienna])
    return napis


def test_formatuj_napis_bez_znacznikow():
    assert formatuj("Hello World!") == "Hello World"

def test_formatuj_wiele_napisow_bez_znacznikow():
    assert formaruj("hello World", "Hi Python!") == "hello World!\nHi Python"

def test_formatuj_napis_bez_znacznikow_ale_ze_zmiennymi_jako_argumenty():
    assert formatuj("Hello World", name="John", lastname="Kovalsky") == "Hello World"

def test_formatuj_napis_ze_zmienna():
    assert formaruj("Hello $name", name="John") == "Hello John"
    assert formaruj("Hello $name $lastname", name="John", lastname="Kovalsky") == "Hello John Kovalsky"


