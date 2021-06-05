
# WEJŚCIA = wychowawca, nauczyciel, uczen, koniec

# wychowawcy(imie, klasy) = pokazuje uczniow w klasie (imiona)
# nauczyciele (imie, przedmiot, klasy) = wychowawcy jego klas
# uczniowie (imie,klasa) = nauczyciel i przedmiot
# klasy = wychowawca i uczniowie w tej klasie
# imiona
# przednmioty
# WYJŚCIA: KLASA > WYCHOWAWCY I UCZNIOWIE TEJ KLASY
#          WYCHOWAWCA > UCZNIOWIE TEGO WYCHOWAWCY
#          NAUCZYCIEL > WYCHOWAWCY JEGO KLAS
#          UCZEN > JEGO LEKCJE I NAUCZYCIELE TYCH LEKCJI

# akcja = input()
# imie = input()
# klasa = input()
# przedmiot = input()
uczniowie = []
nauczyciele = []
wychowawcy = []
przedmioty = []
klasy = []
klasy_wych = []


while True:
    akcja = input()
    if akcja == "wychowawca":
        imie = input()
        klasa = input()
        klasy_wych.append(klasa)
        wychowawcy.append({imie:klasy_wych})
        klasy.append(klasa)

    elif akcja == "uczen":
        imie = input()
        klasa = input()
        uczniowie.append({imie:klasa})

    elif akcja == "nauczyciel":
        imie = input()
        przedmiot = input()
        klasa = input()
        nauczyciele.append(imie)
        przedmioty.append(przedmiot)
        klasy.append(klasa)

    elif akcja == "koniec":
        break

print(wychowawcy)
print(nauczyciele)
print(uczniowie)
print(przedmioty)
print(klasy)
