# START TASK - Lecția OOP1: Clase și Obiecte
# Timp estimat: 20 minute
# Obiectiv: Înțelegerea conceptelor de bază ale OOP în Python

print("=== START TASK - OOP1: CLASE ȘI OBIECTE ===\n")

# Exercițiul 1: Prima ta clasă
# Creează o clasă simplă numită "Persoana" cu:
# - Un atribut "nume" și "varsta"
# - O metodă "saluta" care printează un mesaj de salut

class Persoana:
    def __init__(self, nume, varsta):
        self.nume = nume
        self.varsta = varsta
        # COMPLETEAZĂ AICI - inițializează atributele
    
    
    def saluta(self):
        # COMPLETEAZĂ AICI - printează un mesaj de salut
        print(f"Salut, ma numesc {self.nume} si am varsta {self.varsta}")
        # Exemplu: "Salut, mă numesc [nume] și am [varsta] ani"
 

# Testare Exercițiul 1:
persoana1 = Persoana("Ana", 25)
persoana1.saluta()
# Output așteptat: "Salut, mă numesc Ana și am 25 ani"


# Exercițiul 2: Clasa Câine
# Creează o clasă "Caine" cu:
# - Atribute: nume, rasa, varsta
# - Metode: latra(), doarme(), joaca()

class Caine:
    def __init__(self, nume, rasa, varsta):
        # COMPLETEAZĂ AICI
        self.nume = nume
        self.rasa = rasa
        self.varsta = varsta
        
    
    def latra(self):
        # COMPLETEAZĂ AICI - printează "[nume] face: Ham! Ham!"
        print(f"{self.nume} face: Ham! Ham!")
    
    
    def doarme(self):
        # COMPLETEAZĂ AICI - printează "[nume] doarme liniștit..."
        print(f"{self.nume} doarme linistit..")
        
    
    def joaca(self):
        # COMPLETEAZĂ AICI - printează "[nume] se joacă cu mingea!"
        print(f"{self.nume} se joaca cu mingea")
        
# Testare Exercițiul 2:
rex = Caine("Rex", "Golden Retriever", 3)
rex.latra()
rex.doarme()
rex.joaca()


# Exercițiul 3: Clasa Calculator Simplu
# Creează o clasă "Calculator" cu:
# - Un atribut "rezultat" (inițial 0)
# - Metode: aduna(numar), scade(numar), afiseaza_rezultat()

class Calculator:
    def __init__(self):
        # COMPLETEAZĂ AICI - inițializează rezultat cu 0
        pass
    
    def aduna(self, numar):
        # COMPLETEAZĂ AICI - adaugă numărul la rezultat
        pass
    
    def scade(self, numar):
        # COMPLETEAZĂ AICI - scade numărul din rezultat
        pass
    
    def afiseaza_rezultat(self):
        # COMPLETEAZĂ AICI - printează rezultatul curent
        pass

# Testare Exercițiul 3:
# calc = Calculator()
# calc.aduna(10)
# calc.aduna(5)
# calc.scade(3)
# calc.afiseaza_rezultat()  # Ar trebui să afișeze: 12


# Exercițiul 4: Clasa Carte
# Creează o clasă "Carte" cu:
# - Atribute: titlu, autor, numar_pagini
# - Metode: afiseaza_info(), este_groasa() (returnează True dacă are >300 pagini)

class Carte:
    def __init__(self, titlu, autor, numar_pagini):
        # COMPLETEAZĂ AICI
        pass
    
    def afiseaza_info(self):
        # COMPLETEAZĂ AICI - afișează toate informațiile despre carte
        pass
    
    def este_groasa(self):
        # COMPLETEAZĂ AICI - returnează True dacă cartea are peste 300 de pagini
        pass

# Testare Exercițiul 4:
# carte1 = Carte("1984", "George Orwell", 350)
# carte1.afiseaza_info()
# print(f"Este o carte groasă? {carte1.este_groasa()}")