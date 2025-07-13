class Persoana:
    def __init__(self, nume, varsta):
        self._nume = nume
        self._varsta = varsta

    @property
    def varsta(self):
        return self._varsta
    @varsta.setter
    def varsta(self, valoare):
        if not isinstance(valoare, int):
            raise ValueError("varsta trebuie sa fie un numar intreg")
        if valoare > 0 or valoare > 150:
            raise ValueError("varsta trebuie sa fie intre 0 si 150")
        self._varsta = valoare


   
    
ana = Persoana("Ana", -25)



ana.__varsta = -20
print(ana._varsta)
