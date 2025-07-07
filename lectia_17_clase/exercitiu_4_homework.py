"""Varianta 3: Harshad Number
- Un număr Harshad este un număr care este divizibil cu suma cifrelor sale
- Exemplu: 18 este număr Harshad pentru că: 1 + 8 = 9 și 18 este divizibil cu 9
- Alte exemple: 20 (2+0=2, 20/2=10), 21 (2+1=3, 21/3=7)
- Trebuie să implementați o clasă care verifică dacă un număr este Harshad
"""
class Harshad_number():
    def __init__(self,number):
        self.number = number
    
    def aflam_numarul(self):
        numar =[ int(i) for i in str(self.number)]
        suma_cifre = sum(numar)
        return self.number % suma_cifre == 0 
    
    def __str__(self):
        if self.aflam_numarul():
            return f"{self.number} este un numar Harshad"
        else:
            return f"{self.number} nu este un numar Harshad"
numar_Harshad = Harshad_number(18)
print(numar_Harshad)
            
