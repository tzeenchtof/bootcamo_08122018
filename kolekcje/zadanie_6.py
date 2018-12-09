liczby = [5,2,1,4,3]


indeks_min, indeks_max = None, None

for indeks in range(len(liczby)):
    if indeks_min is None or liczby[indeks] < liczby[indeks_min]:
        indeks_min = indeks
    if indeks_max is None or liczby[indeks] > liczby[indeks_max]:
        indeks_max = indeks
# temp = liczby[0]
# liczby[0]= liczby[2]
# liczby[2] = temp

# liczby[0], liczby[2] = liczby[2], liczby[0]

# for el in liczby
   # pass

liczby[indeks_max], liczby[indeks_min] = liczby[indeks_min], liczby[indeks_max]

# for i in range(len(liczby)):
#    liczby[i]


# print(liczby)

assert liczby == [1,2,5,4,3]