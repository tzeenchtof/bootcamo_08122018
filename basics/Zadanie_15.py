# from random import randint
# from random import choice
#
# lista = [1, 10]
#
# print(choice(lista))
#
# x = randint(1, 10)
# y = randint(1, 10)

# odleg = abs(Sx - Gx) + abs(Sy - Gy)
from random import randint

gracz_x = randint(1, 10)
gracz_y = randint(1, 10)
skard_x = randint(1, 10)
skard_y = randint(1, 10)


min_l_krokow_po_wyl = abs(skard_x-gracz_x) + abs(skard_y - gracz_y)
liczba_krokow = 0
DEBUG = True


while True:
    min_l_krokow_przed_ruchem = abs(skard_x - gracz_x) + abs(skard_y - gracz_y)
    print (f"Twoja pozycja to: {gracz_x}, {gracz_y}")

    if DEBUG:
        print(f"Pozycja skarbu to:  {skard_x}, {skard_y}")


    kierunek = input("Podaj kierunek w-góra, s-dół, a-lewo, d-prawo")
    if kierunek == "w":
        gracz_y =+ 1

    elif kierunek == "s":
        gracz_y -= 1

    elif kierunek == 'a':
        gracz_x -= 'a'

    elif kierunek == 'd':
        gracz_x += 1
        liczba_krokow += 1
        min_l_krokow_po_ruchu = abs(skard_x-gracz_x) + abs(skard_y-gracz_y)

      if gracz_x < 1 or gracz_y < 1 or gracz_x > 10 or gracz_y > 10:
          break

        if gracz_x == skard_x and gracz_y == skard_y:
            print("Wygrałeś!!")
            print(f"Minimalna liczba kroków wynosiła: {min_l_krokow_po_wyl}")
        print(f"Zrobiłeś kroków: {liczba_krokow}")
        break

    los = randint(1, 5)
    if los != 3:
        if min_l_krokow_po_ruchu < min_l_krokow_przed_ruchem:
            print("Ciepło")
        else:
            print("Zimno")

    if liczba_krokow >= min_l_krokow_po_wyl * 2:
skard_x = randint(1, 10)
skard_y = randint(1, 10)

print("Prekroczyłeś dopusdzczalną liczbę kroków skarb zmienił położenie")