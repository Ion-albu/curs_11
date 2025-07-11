class Calculator:
    @staticmethod
    def aduna(a,b):
        suma = a + b
        return suma
    @staticmethod
    def scade(a,b):
        diferenta = a - b
        return diferenta
    @staticmethod
    def impartirea(a,b):
    
        if b> 0:
            catul = a /b
            return catul
        else:
            return f"nu se face impartirea la 0"
    def incercam(self,a,b):
        return Calculator.impartirea(a,b)
    @staticmethod
    def inmulteste(a,b):
        produsul = a * b
        return produsul
print(f"Suma este: {Calculator.aduna(3,3)}")
print(f"Diferenta este: {Calculator.scade(10,5)}")
print(f"Catul este: {Calculator.impartirea(8,0)}")
print(f"produsul este: {Calculator.inmulteste(3,3)}")
m = Calculator()
print(m.incercam(8,2))