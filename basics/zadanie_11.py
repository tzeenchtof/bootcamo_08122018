poz_g_x = int(input("podaj położenie gracza"))
poz_g_y = int(input("podaj pozycję gracza"))

#czy jest poza planszą

if poz_g_x < 0 or poz_g_x > 100 or poz_g_y < 0 or poz_g_y > 100:
    print ("poza planszą")

elif poz_g_x > 90 and poz_g_y > 90:
    print("jesteś w prawym górnym rogu")

elif poz_g_x > 90 and poz_g_y < 10:
    print("jesteś w dolnym P rogu")

elif poz_g_x < 10 and poz_g_y < 10:
    print("jestes w dolnym L rogu")

elif poz_g_x < 10 and poz_g_y > 90:
    print("jeteś w górnym L rogu")

elif poz_g_x < 10:
    print("jesteś na lewej krawędzi")
elif poz_g_x > 90:
    print("jesteś na praw krawędzi")
elif poz_g_y < 10:
    print("dolna krawędz")
elif poz_g_y > 90:
    print("gorna krawędż")
else:
    print("jesteś w centrum")
