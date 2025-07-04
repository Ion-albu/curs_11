class Exemplu:
    def __init__(self,valoare):
        self.valoare = valoare
    
    def afiseaza(self):
        print(f"afisam valoarea  noastra: {self.valoare}")
    
    def modifica_valoare(self, valoare_noua):
        self.valoare = valoare_noua
        self.afiseaza()

obj = Exemplu(8)
obj.afiseaza()
obj.modifica_valoare(20)