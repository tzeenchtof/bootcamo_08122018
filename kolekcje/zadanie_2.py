# i=0
# while i <10:
#     liczba = input("Podaj liczbę lub k by zakończyć")
#     if liczba == 'k':
#         break
#     liczba = int(liczba)
#     liczby.append(liczba)
#     i =+ 1
#
#     print("średnia wynosi: ", sum(liczby)/len(liczby))
#

dane = input("podaj liczby, rozdziel je spacjami")
dane = dane.split()


dane2 = []

for d in dane:
    dane2.append(int(d))

#dane = [int(d) for d in dane]
dane = map(int, dane)
print(dane)