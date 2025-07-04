"""
Varianta 1: Perfect Number
- Un număr perfect este un număr natural care este egal cu suma divizorilor săi proprii (toți divizorii pozitivi în afară de numărul însuși)
- Exemplu: 28 este număr perfect pentru că: 1 + 2 + 4 + 7 + 14 = 28
- Alte exemple: 6 (1 + 2 + 3 = 6), 496 (1 + 2 + 4 + 8 + 16 + 31 + 62 + 124 + 248 = 496)
- Trebuie să implementați o clasă care verifică dacă un număr este perfect
"""
class Nrperfect:
    def __init__(self,number):
        self.number = number
        self.divizori = []

    def cauta_numere(self):
        for i in range(1, self.number //2 +1):
            if self.number % i == 0:
                self.divizori.append(i) 

    def afiseaza_nr(self):
        print(f"numarul perfect este: {self.number} iar divizorii lui sunt: {self.divizori}")

nr = Nrperfect(28)
nr.cauta_numere()
nr.afiseaza_nr()

