# napisz program który posortuje przy pomocy algorytmu sortowanie przez wybieranie

liczby = [5, 2, 4, 7, 8, 3, 9, 0, 1]

for i in range(len(liczby)):
    indeks_minimum = i
    for j in range(i, len(liczby)):
         if liczby[j] < liczby[indeks_minimum]:
             indeks_minimum = j

    liczby[i], liczby[indeks_minimum] = liczby[indeks_minimum], liczby[i]

print(liczby)

# assert liczby == [5, 2, 4, 7, 8, 3, 9, 0, 1]

# indeks_minimum = 0
# for j in range(len(liczby)):
#     if liczby[j] < liczby[indeks_minimum]:
#         print("Znalazłem minimum")
#         print("Nowa wartość minimum to: ", liczby[i])
#         print("Nowy indeks minimum to:", i)
#         indeks_minimum = i

# liczby[0], liczby[indeks_minimum]= liczby[indeks_minimum], liczby[0]
#
# print(liczby)
# print("-"*40)
#
# print (liczby[0])
# print (liczby[7])
#
#
# # temp = liczby[7]
# # liczby[7] = liczby[0]
# # liczby[0] = temp
#
# liczby[0], liczby[7] = liczby[7], liczby[0]
# print(liczby)