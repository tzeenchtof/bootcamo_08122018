znalezion_maksimum = None
znalezion_minimum = None
liczba = None
while True:

    komenda = input("podaj liczbę lub k by zakończyć: ")
    if komenda == 'k':
        break
    if len (komenda) > 0 and komenda[0] == '-' and komenda[1:].isdigit():
        liczba = int(komenda[1:])
        liczba = -liczba
    elif komenda.isdigit():
        liczba = int(komenda)
    else:
        print("nie podałeś liczby")


    if liczba or liczba == 0:
        liczba = int(komenda)
        if znalezion_maksimum is None or liczba > znalezion_maksimum:
            znalezion_maksimum = liczba
        if znalezion_minimum is None or liczba < znalezion_minimum:
            znalezion_minimum = liczba

        print("znalezione maksimum to: ", znalezion_maksimum)
        print("znalezione minimum to: ", znalezion_minimum)
    else:
        print("nie podałeś liczby")