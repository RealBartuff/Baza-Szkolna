
import sys

uczniowie = []
nauczyciele = {}
wychowawcy = {}

while True:
    akcja = input().strip()
    if akcja == "wychowawca":
        imie = input()
        wychowawcy[imie]=[]
        while True:
            klasa = input()
            if klasa:
                wychowawcy[imie].append(klasa)
            else:
                break

    elif akcja == "nauczyciel":
        imie = input()
        nauczyciele[imie]={}
        nauczyciele[imie]["przedmiot"]=input()
        nauczyciele[imie]["klasy"] = []
        while True:
            klasa = input()
            if klasa:
                nauczyciele[imie]["klasy"].append(klasa)
            else:
                break

    elif akcja == "uczen":
        imie = input()
        klasa = input()
        uczniowie.append({"imie":imie, "klasa":klasa})

    elif akcja == "koniec":
        break


if len(sys.argv[1]) == 2:
    wychowawca = ""
    uczniowie_klasa = []
    for imie in wychowawcy:
        if sys.argv[1] in wychowawcy[imie]: # jeśli NUMER KLASY zawiera się w liście klas danego wychowawcy
            wychowawca = imie
    for uczen in uczniowie:
        if sys.argv[1] == uczen["klasa"]:
            uczniowie_klasa.append(uczen["imie"])
    print(wychowawca)
    for uczn in uczniowie_klasa:
        print(uczn)

if sys.argv[1] in wychowawcy:
    klasy_wychowawcy = wychowawcy[sys.argv[1]]
    uczniowie_wychowawcy = []
    for uczen in uczniowie:
        if uczen["klasa"] in klasy_wychowawcy:
            uczniowie_wychowawcy.append(uczen["imie"])
    for ucz in uczniowie_wychowawcy:
        print(ucz)

if sys.argv[1] in nauczyciele:
    klasy_nauczyciel = nauczyciele[sys.argv[1]]["klasy"]
    wych_klas = []
    for wych in wychowawcy:
        for klasa in wychowawcy[wych]:
            if klasa in klasy_nauczyciel:
                wych_klas.append(wych)
                break
    for wych in wych_klas:
        print(wych)

imiona_ucz = []
for uczen in uczniowie:
    imiona_ucz.append(uczen["imie"])
if sys.argv[1] in imiona_ucz:
    klasa_ucznia = ""
    for uczen in uczniowie:
        if uczen["imie"] == sys.argv[1]:
            klasa_ucznia = uczen["klasa"]
            break
    for nauczyciel in nauczyciele:
        if klasa_ucznia in nauczyciele[nauczyciel]["klasy"]:
            print(nauczyciele[nauczyciel]["przedmiot"])
            print(nauczyciel)
