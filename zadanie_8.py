wys = int(input("podaj wysokość: "))
szer = int(input("podaj wysokość: "))
dlug = int(input("podaj długość: "))

obj = int(wys * szer * dlug)

print (f"objętość paczki: {obj}")
#print (f"czy większa od jednego litra: {obj > 1000}")

if obj > 1000:
    print ("objętość jest większa niż 1 Litr")

elif obj < 500:
    print ("objętość mniejsza niż 0,5L")

else:
    print("objętość jest mniejsza niż 1 litr")

print ("koniec programu")