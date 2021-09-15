class Uczen:
    def __init__(self, kid_name, clas_name):
        self.kid_name = kid_name
        self.clas_name = clas_name
        self.type = "uczen"

    def write(self):
        print(self.kid_name)


class Wychowawca:  # tworze pustą class Wychowawca
    def __init__(
        self, wych_name, classes_names
    ):  # Przypisuje, ze Wychowawca zawiera w sobie wych_name i class_names
        self.wych_name = wych_name  # definiuje wych_name i class_names
        self.classes_names = classes_names
        self.type = "wychowawca"

    def write(self):  # ta funkcja wypisuje \/
        print(self.wych_name)  # /\ w tym wypadku wych name


class Nauczyciel:
    def __init__(self, teach_name, subject, classes_names):
        self.teach_name = teach_name
        self.subject = subject
        self.classes_names = classes_names
        self.type = "nauczyciel"

    def write(self):
        print(self.subject)
        print(self.teach_name)


def wrapper(
    akcja, wychowawcy, nauczyciele, uczniowie
):  # ta funkcja zawiera w sobie parametry akcja(czyli argv, i kolejno trzy słowniki)
    if len(akcja) == 2:
        wychowawca = ""
        uczniowie_klasa = []
        for imie, dane in wychowawcy.items():
            if akcja in dane.classes_names:
                wychowawca = imie
        for uczen, dane2 in uczniowie.items():
            if akcja == dane2.clas_name:
                uczniowie_klasa.append(dane2)
        print(wychowawca)
        for uczn in uczniowie_klasa:
            uczn.write()  # .write() wypisuje nam zgodnie z formatem zawartym w klasie

    elif akcja in nauczyciele:
        nauczyciel = nauczyciele[akcja]
        wych_klas = []
        for wych, dane in wychowawcy.items():
            for klasa in wychowawcy[wych].classes_names:
                if klasa in nauczyciel.classes_names:
                    wych_klas.append(dane)
                    break
        for wych in wych_klas:
            wych.write()

    elif akcja in wychowawcy:
        wychowawca = wychowawcy[akcja]  # pobieramy klasy wychowawcy
        uczniowie_wychowawcy = []  # inicjujemy liste uczniow wychowawcy
        for uczen, dane in uczniowie.items():
            if dane.clas_name in wychowawca.classes_names:
                uczniowie_wychowawcy.append(dane)
        for ucz in uczniowie_wychowawcy:
            ucz.write()

    elif akcja in uczniowie:
        nauczyciele_klasy = []
        klasa_ucznia = ""
        for uczen, dane in uczniowie.items():
            if uczen == akcja:
                klasa_ucznia = dane.clas_name
        for teach_name, dane2 in nauczyciele.items():
            if klasa_ucznia in dane2.classes_names:
                nauczyciele_klasy.append(dane2)
        for nauczyciel in nauczyciele_klasy:
            nauczyciel.write()
