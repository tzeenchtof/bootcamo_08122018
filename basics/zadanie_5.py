#deklaracje zmiennych


miasto_a = input("Podaj nazwę miasta A: ")
miasto_b = input("Podaj nazwę miasta B: ")

dystans = int(input(f"Podaj dystans pomiędzy {miasto_a} - {miasto_b}"))

cena_P = float(input("Podaj cenę paliwa: "))
spalanie = float(input("spalanie na 100 km: "))

koszt = (dystans / 100) * spalanie * cena_P

print (f"{miasto_a} - {miasto_b} to {koszt} PLN")

#OPERATORY LOGICZNE
#operatory porównania
#==, <, >, <=, >=, !=