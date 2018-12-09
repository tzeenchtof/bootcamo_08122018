liczba = int(input("podaj liczbę do sprawdzenia: "))

# info = f"""
# liczba jest podzielna przez 2, {liczba%2 == 0}
# liczba jest podzielna przez 3, {liczba%3 == 0}
# liczba jest większa od 10, {liczba > 10} lub jest to siedem {or } {liczba == 7}"""
#
# print (info)

wynik = (liczba == 7) or (liczba % 2 == 0 and liczba % 3 == 0 and liczba > 10)