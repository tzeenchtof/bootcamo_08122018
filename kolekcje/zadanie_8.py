# napisz program zliczający liczbę znaków w podanym przez użytkownika napisie pomiędzy nawiasami <>. Nawiasy mogą wystąpić tylko raz

# Ala ma <kota>, a kot ma Alę

tekst = input("Podaj tekst: ")

# tekst1 = "Ala ma kota"
# tekst2 = "Ala<ma> kota"
# tekst3 = "Ala <> ma kota"

dlugosc = 0
licz = False
for znak in tekst:
    if znak == "<":
        licz = True
    elif znak == ">":
        licz = False


    elif licz:
        dlugosc += 1
# print(dlugosc == 0)
#assert dlugosc1 == 0

print (f"liczba znaków pomiędzy <> wynosi {dlugosc}")