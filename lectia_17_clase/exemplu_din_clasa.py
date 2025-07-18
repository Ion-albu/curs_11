class Om():
    def __init__(self, nume, data_nast, adresa , inaltime):
        self.nume = nume
        self.data_nast = data_nast
        self.adresa = adresa
        self.inaltime = inaltime

    def se_muta(self, adresa_noua):
        self.adresa = adresa_noua
    
    def creste(self, inaltime_noua):
        self.inaltime = inaltime_noua  
    
    def __str__(self):
        return f"Numele: {self.nume}, Data de nastere: {self.data_nast}, Adresa de locuinta: {self.adresa}, Inaltimea: {self.inaltime}"
    
    def __repr__(self):
        return f"Om = (name='{self.nume}', Data de nastere='{self.data_nast}', Adresa de locuinta='{self.adresa}', Inaltimea='{self.inaltime}')"
    

om1 = Om("Ion", 1995, "Chiscareni", 179)
om2 = Om("Sorin", 1996, "Balti", 180)

print(om1)
om1.se_muta("Saliste")
print(om1.adresa)
print(repr(om1))
