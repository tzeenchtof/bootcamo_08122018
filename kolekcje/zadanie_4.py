
licznik = 0

for i in range(0, 101):
    if i % 3 == 0 or i % 5 ==0:
        print(i)
        licznik += 1

        print(licznik)

# lista = [i for i in range (0, 101) if i % 3 == 0 or i % 5 == 0]
# print("\n".join(map(str, lista)))
#
# print(len(lista))
