""""
Varianta 2: Armstrong Number
- Un număr Armstrong este un număr care este suma cifrelor sale ridicate la puterea 3
- Exemplu: 371 este număr Armstrong pentru că: 3^3 + 7^3 + 1^3 = 27 + 343 + 1 = 371
- Alte exemple: 153, 370, 407
- Trebuie să implementați o clasă care verifică dacă un număr este Armstrong
"""
class Armstrong_number:
    def __init__(self,number):
        self.number = number
    
        
    def is_armstrong(self):
        num_str = str(self.number)
        suma = sum(int(cifra)**3 for cifra in num_str)
        return suma == self.number
    
    def __str__(self):
        if self.is_armstrong():
            return f"{self.number} este un numar Armstrong"
        else:
            return f"{self.number} nu este un numar Armstrong."
        
           

afiseaza = Armstrong_number(241)
print(afiseaza)
        