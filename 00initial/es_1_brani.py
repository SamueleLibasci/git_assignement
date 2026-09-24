class Brano:
    def __init__(self, titolo, autore, durata):
        self._titolo = titolo
        self._autore = autore
        self._durata = durata

    @property
    def titolo(self):
        return self._titolo

    @titolo.setter
    def titolo(self, valore):
        self._titolo = valore

    @property
    def autore(self):
        return self._autore

    @autore.setter
    def autore(self, valore):
        self._autore = valore

    @property
    def durata(self):
        return self._durata

    @durata.setter
    def durata(self, valore):
        self._durata = valore

    def __str__(self):
        return f"{self.titolo} - {self.autore} ({self.durata} sec)"


if __name__ == "__main__":
    newBrano = Brano("Imagine", "John Lennon", 180)
    print(newBrano)
