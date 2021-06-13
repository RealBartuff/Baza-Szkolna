import sys

from bazaklasy import Wychowawca, Nauczyciel, Uczen, wrapper

with open("in.txt") as data:

    wychowawcy = {}
    nauczyciele = {}
    uczniowie = {}

    while True:
        stanowisko = data.readline().rstrip()
        if not stanowisko:
            break

        elif stanowisko == "wychowawca":
            imie = data.readline().rstrip()
            klasy = []
            while True:
                klasa = data.readline().rstrip()
                if klasa:
                    klasy.append(klasa)
                else:
                    break
            wychowawcy[imie] = Wychowawca(imie, klasy)

        elif stanowisko == "nauczyciel":
            imie = data.readline().rstrip()
            przedmiot = data.readline().rstrip()
            klasy = []
            while True:
                klasa = data.readline().rstrip()
                if klasa:
                    klasy.append(klasa)
                else:
                    break
            nauczyciele[imie] = Nauczyciel(imie, przedmiot, klasy)

        elif stanowisko == "uczen":
            imie = data.readline().rstrip()
            klasa = data.readline().rstrip()
            uczniowie[imie] = Uczen(imie, klasa)


wrapper(sys.argv[1], wychowawcy, nauczyciele, uczniowie)
