# w sesji interaktywnego środowiska stwórz
# następujące struktury danych
# korzystając ze skróconej wersji zapisu

# listę zawierającą liczby zmiennoprzecinkowe od 0.0 do 1.0 z krokiem 0.1

print([x/10 for x in range(11)])

# zbiór tupli zawierających 3 elementy - daną liczbę, jej kwadrat i jej sześcian - w przedziale od -10 do 10

print({(x, x**2, x**3) for x in range(-10, 11)})

# słownik mapujący napisy na ich długość powstały ze zbiory napisów

napisy = {"Alama kota", "kotr ma alę", "zażółć gęślą jażń"}
print({x: len(x) for x in napisy})




