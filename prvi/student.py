class Covek:
    jeliZiv = "Jeste"
    jedeLi = True
    noge = 2


class Student(Covek):
    ime = None
    prezime = None
    indeks = None
    prosek = None

    def __init__(self, ime, prezime, indeks, prosek):
        self.prosek = prosek + 0.5
        self.indeks = indeks
        self.prezime = prezime
        self.ime = ime

    def uci(self):
        print("Student {} uci.".format(self.ime))

    def partija(self):
        print("Student {} partija.".format(self.ime))
