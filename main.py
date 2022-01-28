'''
3.2 Feladat
Írj egy programot, amely tartalmaz egy 'harommal_oszthatok' nevű függvényt, amely a paraméterként átvett listában megvizsgálja, hogy hány darab hárommal osztható szám van, és ezzel az értékkel tér vissza! 
A program tartalmazza a függvény hívását is!

Alakítsd át az előző programot úgy, hogy a felhasználó által megadott számokat tárolja el a program egy listában, és ezt értékelje ki a függvény! 
Az adatbeolvasás addig tartson, míg a felhasználó negatív számot nem ad meg!
'''
szamok = []

def harommal_oszthatok():
  while True:
    bekert = int(input("Adj meg egy számot! "))
    if bekert < 0:
      break
    else:
      szamok.append(bekert)
    szamlalo = 0
    for szam in szamok:
      if szam % 3 == 0:
        szamlalo += 1
  return print(szamlalo)

harommal_oszthatok()
