liczba = int(input("podaj liczbę: "))

print()

info = f"""
("podana liczba jest większa od 10:", {liczba > 10})
("podana liczba jest mniejsza równa 15:", {liczba <= 15})
("podana liczba jest podzielna przez 2:", {liczba%2 == 0})"""

print (info)

x = 2
y = 5

print (x > 1 and y > 1)
print (x > 1 or y > 1)