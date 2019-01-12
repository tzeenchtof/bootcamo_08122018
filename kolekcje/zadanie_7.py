# Napisz program zliczający liczbę wystąpień samogłosek (aeiouy) w -p0odanym przez użytkownika napisie

# text = input("Podaj tekst: ")
tekst = "Ala ma kota eaiouy"
ile_samogłosek = 0
SAMOGLOSKI = 'eaiouy'
for litera in tekst:
    if litera in SAMOGLOSKI:
        ile_samogłosek += 1


ile_samoglosek2 = 0
for samogloska in SAMOGLOSKI:
    ile_samoglosek2 += tekst.lower().count(samogloska)
print(ile_samogłosek == 11)
print(ile_samoglosek2 == 11)