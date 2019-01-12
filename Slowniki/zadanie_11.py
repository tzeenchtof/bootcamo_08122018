# Napisz program zliczający liczbę unikalnych liczb wprowadzonych przez użytkownika.
# Sprawdż jak dużo z tych liczb jest liczbami parzstymi w zakresie 0-100
# w tym celu skorzystaj z operatora iloczynu


# unik_licz = input("Podaj unikalne liczby: ")

liczby = set()
parzyste = set(range(0, 100, 2))
while True:
    komenda = input("Podaj liczbę lub [k] by zakońćzyć: ")
    if komenda == 'k':
        break
    else:
        liczby.add(int(komenda))

# print(liczby)

print("Liczbn unikalnych jest: ", len(liczby))
print("Z tego parzystych jest: ", len(liczby & parzyste))