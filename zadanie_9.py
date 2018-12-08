import datetime

rok_ur = int(input("podaj rok urodzenia"))
year = datetime.datetime.now().year
if rok_ur + 18 <= year:
    print("jesteś pełnoletni !!")

else:
    print("jesteś nieletni")
