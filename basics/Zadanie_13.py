# dni_tyg = int(input("podaj ilość dni tygodnia"))
# temper = int(input(f"podaj temperaturę" {dni_tyg})
#
# while dni_tyg <=7:
#     print()
#

ILE_DNI = 7

temp = 0
i = 1

while i <= ILE_DNI :

    komenda = input(f"Podaj Temperaturę w dniu {i} lub [k] by zakończyć")
    if komenda == "k":
                  break
    temp_i = float(komenda)
    temp =+ temp_i
    i += 1
print("Średenia teperatura wynosiła: ", temp/(i-1))