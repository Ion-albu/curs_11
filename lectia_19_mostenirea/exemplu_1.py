class Animal:
    def __init__(self,nume,varsta,greutate):
        self.nume = nume
        self.varsta = varsta
        self.greutate = greutate
    
    def mananca(self):
        self.greutate += 0.2
        print(f"{self.nume} mananca si cantareste acum {self.greutate} kg")

    def descrie(self):
        return "sunt un animal generic"
    
class Pisica(Animal):
        def zgaraie(self):
             return f"{self.nume} zgaraie!"
        def __str__(self):
             return f"{self.nume} are varsta de {self.varsta} si cantereste {self.greutate}"
        
class Delfin(Animal):
        def inoata(self):
            return f"{self.nume} inoata!"
        
class Pasare(Animal):
        def zboara(self):
            return f"{self.nume} zboara"
        
pisica = Pisica("Ion", 26, 52)
delfin = Delfin("Vasile", 15, 62)
pasare = Pasare("porumbel", 4, 15)

print(pisica)
print(delfin.varsta)
print(pasare.greutate)

pisica.mananca()

print(pisica.zgaraie())
print(delfin.inoata())
print(pasare.zboara())